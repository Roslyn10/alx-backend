import { createClient, print } from 'redis';

const redisClient = createClient();

redisClient.on('error', (err) => {
	console.log('Redis clinet on connected to the server:', err);
});

redisClient.on('connect', () => {
	console.log('Redis client connected to the server');
});



redisClient.hset('HolbertonSchools', 'Portland', '50', print);
redisClient.hset('HolbertonSchools', 'Seattle', '80', print);
redisClient.hset('HolbertonSchools', 'New York', '20', print);
redisClient.hset('HolbertonSchools', 'Bogota', '20', print);
redisClient.hset('HolbertonSchools', 'Cali', '40', print);
redisClient.hset('HolbertonSchools', 'Paris', '2', print);

redisClient.hgetall('HolbertonSchools', function (error, result) {
	if (error) {
		console.log(error);
		throw error;
	}
	console.log(result);
});
