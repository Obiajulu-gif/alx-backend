import { createClient, print } from "redis";
const client = createClient();

// handle sucessfull connection
client.on("connect", () => {
	console.log("Redis client connected to the server");
});

// handle connection error
client.on("error", (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, print); // redis.print logs the operation result
}

// Function to display the value for a given key from Redis
function displaySchoolValue(schoolName) {
	client.get(schoolName, (err, reply) => {
		if (err) throw err;
		console.log(reply); // Logs the value of the key
	});
}

// Call functions to demonstrate
displaySchoolValue("Holberton"); // Initially will be null if not set
setNewSchool("HolbertonSanFrancisco", "100"); // Sets the new key-value
displaySchoolValue("HolbertonSanFrancisco"); // Logs '100'
