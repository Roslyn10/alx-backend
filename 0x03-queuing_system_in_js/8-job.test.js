import { expect } from 'chai';
import sinon from 'sinon';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', function () {
    let queue;
    let createJobStub;
    let job;
    let jobSaveStub;
    let jobOnStub;

    beforeEach(() => {
        queue = {
            create: sinon.stub()
        };

        job = {
            id: 1,
            priority: sinon.stub().returnsThis(),
            attempts: sinon.stub().returnsThis(),
            save: sinon.stub(),
            on: sinon.stub()
        };

        createJobStub = queue.create.returns(job);

        jobSaveStub = sinon.stub(job, 'save');

        jobOnStub = sinon.stub(job, 'on').returns(job);
    });

    afterEach(() => {
        sinon.restore();
    });

    it('should throw an error if jobs is not an array', () => {
        const invalidJobs = 'Not an array';
        expect(() => createPushNotificationsJobs(invalidJobs, queue)).to.throw(Error, 'Jobs is not an array');
    });

    it('should create jobs in the queue and log events', () => {
        const jobs = [
            { phoneNumber: '1234567890', message: 'Hello!' },
            { phoneNumber: '0987654321', message: 'Your order is ready!' }
        ];

        const logStub = sinon.stub(console, 'log');

        createPushNotificationsJobs(jobs, queue);

        expect(queue.create.calledTwice).to.be.true;

        expect(logStub.calledWith('Notification job created: 1')).to.be.true;

        job.on.withArgs('complete').yields();
        job.on.withArgs('failed').yields('Error');
        job.on.withArgs('progress').yields(50);

        job.on('complete')();
        job.on('failed')();
        job.on('progress')(50);

        expect(logStub.calledWith('Notification job 1 completed')).to.be.true;
        expect(logStub.calledWith('Notification job 1 failed: Error')).to.be.true;
        expect(logStub.calledWith('Notification job 1 50% complete')).to.be.true;

        logStub.restore();
    });
});

