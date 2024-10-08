import { createQueue} from 'kue';


const queue = createQueue();


const job = queue.create('push_notification_code', {
	phoneNumber: '0559484334',
	message: 'Your account has been registered',
});
job
	.on('enqueue', () => {
		console.log(`Notification job created: ${job.id}`);
	})
	.on('complete', () => {
		console.log('Notification job complete');
	})
	.on('failed', () => {
		console.log('Notification job failed');
	});
job.save();
