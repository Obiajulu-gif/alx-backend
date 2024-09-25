// 8-job.js

export default function createPushNotificationsJobs(jobs, queue) {
	// Check if jobs is an array
	if (!Array.isArray(jobs)) {
		throw new Error("Jobs is not an array");
	}

	// Loop through each job in the jobs array
	jobs.forEach((jobData) => {
		// Create a new job in the queue 'push_notification_code_3'
		const job = queue.create("push_notification_code_3", jobData);

		// Add event listeners for the job
		job
			.on("enqueue", () => {
				console.log(`Notification job created: ${job.id}`);
			})
			.on("complete", () => {
				console.log(`Notification job ${job.id} completed`);
			})
			.on("failed", (errorMessage) => {
				console.log(`Notification job ${job.id} failed: ${errorMessage}`);
			})
			.on("progress", (progress) => {
				console.log(`Notification job ${job.id} ${progress}% complete`);
			});

		// Save the job in the queue
		job.save((err) => {
			if (err) {
				console.log(`Job failed to save: ${err}`);
			}
		});
	});
}
