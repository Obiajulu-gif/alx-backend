import express from 'express';
import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';

// Initialize Express app
const app = express();
const port = 1245;

// Create Redis client and promisify Redis commands
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Create Kue queue
const queue = kue.createQueue();

// Number of seats
let reservationEnabled = true;
const initialSeats = 50;

// Set initial available seats in Redis
async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return parseInt(seats);
}

// Initialize the number of available seats when the app starts
reserveSeat(initialSeats);

// Route to get the current number of available seats
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  // Create a job for the reservation
  const job = queue.create('reserve_seat', {})
    .save((err) => {
      if (!err) {
        return res.json({ status: 'Reservation in process' });
      }
      return res.json({ status: 'Reservation failed' });
    });

  // Log job completion or failure
  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  }).on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

// Route to process the queue
app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();

    // If no seats are available, fail the job
    if (availableSeats <= 0) {
      done(new Error('Not enough seats available'));
      return;
    }

    // Decrease the number of seats
    await reserveSeat(availableSeats - 1);

    // If no seats are left, block further reservations
    if (availableSeats - 1 === 0) {
      reservationEnabled = false;
    }

    done(); 
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
