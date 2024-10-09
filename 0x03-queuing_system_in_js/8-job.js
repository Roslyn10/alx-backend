const kue = require('kue');
const queue = kue.createQueue();

const createPushNotificationsJobs = (jobs, queue) => {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    jobs.forEach((jobData) => {
        const job = queue.create('push_notification_code_3', jobData)
            .priority('normal')
            .attempts(3);

        job.on('enqueue', () => {
            console.log(`Notification job created: ${job.id}`);
        });

        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        });

        job.on('failed', (errorMessage) => {
            console.log(`Notification job ${job.id} failed: ${errorMessage}`);
        });

        job.on('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`);
        });

        job.save((err) => {
            if (err) {
                console.error('Error saving job:', err);
            }
        });
    });
};

export default createPushNotificationsJobs;

