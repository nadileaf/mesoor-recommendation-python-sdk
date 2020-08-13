import unittest
from unittest.mock import AsyncMock

from com.mesoor.mesoor_recommendation import sdk
from mesoor_recommendation_sdk import models, MesoorRecommendation


class SdkTestCase(unittest.IsolatedAsyncioTestCase):
    service = MesoorRecommendation('localhost:50051')
    service.stub.save_candidate = AsyncMock(name='save_job')
    service.stub.save_job = AsyncMock(name='save_job')
    stub_recommend_candidates_by_job_mock = AsyncMock(name='recommend_candidates_by_job')
    recommend_candidates_by_job_result = sdk.RecommendedCandidatesRepresentation(
        candidates=[
            sdk.RecommendedCandidatesRepresentationRecommendedCandidateRepresentation(
                id='foo_id',
                score=0.8,
                reason=sdk.RecommendedCandidatesRepresentationReason(
                    job_name=['asd']
                )
            )
        ]
    )
    stub_recommend_candidates_by_job_mock.return_value = recommend_candidates_by_job_result
    service.stub.recommend_candidates_by_job = stub_recommend_candidates_by_job_mock

    async def test_save_job(self):
        job_detail = models.JobDetail(
            name='foo name',
            description='foo jd',
            employer='foo company',
            degree=models.Degree.本科,
            years=1,
            salary_high=1000,
            salary_low=100,
            publish_date_ts=1597738339072,
            expire_date_ts=1597738339073,
            industries=['foo_ind'],
            location_ids=[123],
            department='foo department',
            categories=['foo_cat']
        )
        job = models.Job(
            job_detail=job_detail,
            status=models.Status.ARCHIVE
        )
        id = 'foo_id'
        await self.service.save_job(
            id=id,
            job=job
        )

    async def test_save_candidate(self):
        basic = models.ResumeBasic(
            location_id=123,
            birthday_ts=1597738339072
        )
        works = [
            models.ResumeWork(
                position='foo name',
                company='foo company',
                description='foo jd',
                department='foo department',
                industry='foo ind',
                responsibility='foo resp',
                start_date_ts=1597738339072,
                end_date_ts=1597738339073,
                until_now=False
            )
        ]
        projects = [
            models.ResumeProject(
                position='foo position',
                company='foo company',
                description='foo jd',
                department='foo department',
                name='foo name',
                responsibility='foo resp',
                start_date_ts=1597738339072,
                end_date_ts=1597738339073,
                until_now=False
            )
        ]
        interns = [
            models.ResumeIntern(
                position='foo name',
                company='foo company',
                description='foo jd',
                department='foo department',
                responsibility='foo resp',
                start_date_ts=1597738339072,
                end_date_ts=1597738339073,
                until_now=False
            )
        ]
        educations = [
            models.ResumeEducation(
                major='foo major',
                degree=models.Degree.本科,
                school='foo school',
                start_date_ts=1597738339072,
                end_date_ts=1597738339073,
                until_now=False
            )
        ]
        resume = models.Resume(
            works=works,
            educations=educations,
            projects=projects,
            interns=interns,
            basic=basic,
            update_date_ts=1597738339072
        )
        candidate = models.Candidate(
            resume=resume,
            status=models.Status.ARCHIVE
        )
        id = 'foo_id'
        await self.service.save_candidate(
            id=id,
            candidate=candidate
        )

    async def test_recommend_candidates_by_job(self):
        job_id = 'foo_id'
        result = await self.service.recommend_candidates_by_job(job_id=job_id)
        self.assertEqual(len(result), 1)


if __name__ == '__main__':
    unittest.main()
