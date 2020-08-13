import unittest

from com.mesoor.mesoor_recommendation import sdk
from mesoor_recommendation_sdk import models


class ModelToSdkRepresentationTestCase(unittest.TestCase):
    def test_job(self):
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
        expect_sdk_representation = sdk.Job(
            job_detail=sdk.JobDetail(name='foo name',
                                     description='foo jd',
                                     employer='foo company',
                                     publish_date_ts=1597738339072,
                                     expire_date_ts=1597738339073,
                                     industries=['foo_ind'],
                                     location_ids=[123],
                                     department='foo department',
                                     years=1,
                                     degree=16,
                                     salary_low=100,
                                     salary_high=1000,
                                     categories=['foo_cat']),
            status=2
        )

        self.assertEqual(job.to_sdk_representation(), expect_sdk_representation)

    def test_candidate(self):
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
        expect_sdk_candidate = sdk.Candidate(
            resume=sdk.Resume(
                works=[
                    sdk.ResumeWork(position='foo name',
                                   company='foo company',
                                   description='foo jd',
                                   department='foo department',
                                   industry='foo ind',
                                   responsibility='foo resp',
                                   start_date_ts=1597738339072,
                                   end_date_ts=1597738339073,
                                   until_now=False)
                ],
                projects=[
                    sdk.ResumeProject(position='foo position',
                                      company='foo company',
                                      description='foo jd',
                                      name='foo name',
                                      responsibility='foo resp',
                                      department='foo department',
                                      start_date_ts=1597738339072,
                                      end_date_ts=1597738339073,
                                      until_now=False)
                ],
                interns=[
                    sdk.ResumeIntern(position='foo name',
                                     company='foo company',
                                     description='foo jd',
                                     responsibility='foo resp',
                                     department='foo department',
                                     start_date_ts=1597738339072,
                                     end_date_ts=1597738339073,
                                     until_now=False)
                ],
                educations=[
                    sdk.ResumeEducation(major='foo major',
                                        degree='本科',
                                        school='foo school',
                                        start_date_ts=1597738339072,
                                        end_date_ts=1597738339073,
                                        until_now=False)
                ],
                basic=sdk.ResumeBasic(location_id=123, birthday_ts=1597738339072),
                update_date_ts=None
            ),
            status=2)

        self.assertEqual(candidate.to_sdk_representation(), expect_sdk_candidate)


if __name__ == '__main__':
    unittest.main()
