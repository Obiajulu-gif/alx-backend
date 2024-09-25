import { createClient } from "redis";
import { promisify } from "util";

const client = createClient();

client.on("connect", () => {
	console.log("Redis client connected to the server");
});

client.on("error", (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`);
});

// Promisify the 'get' method
const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, (err, reply) => {
		if (err) throw err;
		console.log(reply);
	});
}

async function displaySchoolValue(schoolName) {
	try {
		const value = await getAsync(schoolName);
		console.log(value);
	} catch (err) {
		console.log(err);
	}
}

// Call functions to demonstrate
displaySchoolValue('Holberton'); // Initially will be null if not set
setNewSchool('HolbertonSanFrancisco', '100'); // Sets the new key-value
displaySchoolValue('HolbertonSanFrancisco'); // Logs '100'
