import logging
from typing import List

from grpclib.client import Channel

from com.mesoor.mesoor_recommendation import sdk
from . import models
from .errors import RemoteServerError, NotFound

logger = logging.getLogger(__name__)


class MesoorRecommendation:
    def __init__(self, address: str):
        host, port = address.split(':')
        self.channel = Channel(host, int(port))
        self.stub = sdk.MesoorRecommendationControllerStub(self.channel)

    async def save_job(self, id: str, job: models.Job):
        """
        保存职位信息
        :param id: 职位id
        :param job: 职位信息
        :return:
        :exception RemoteServerError
        """
        try:
            return await self.stub.save_job(
                id=id,
                job=job.to_sdk_representation()
            )
        except Exception as e:
            raise RemoteServerError(f'Save job [{id}] error') from e

    async def save_candidate(self, id: str, candidate: models.Candidate):
        """
        保存职位信息
        :param id: 职位id
        :param job: 职位信息
        :return:
        :exception RemoteServerError
        """
        try:
            return await self.stub.save_candidate(
                id=id,
                candidate=candidate.to_sdk_representation()
            )
        except Exception as e:
            raise RemoteServerError(f'Save candidate [{id}] error') from e

    async def recommend_candidates_by_job(self, job_id: str, size: int = 10) -> List[models.RecommendedCandidate]:
        """
        根据职位推荐候选人
        :param job_id: 职位id
        :param size: 候选人最大数量
        :return: 被推荐出来的候选人
        :exception RemoteServerError
        """
        try:
            response = await self.stub.recommend_candidates_by_job(job_id=job_id, size=size)
            result = []
            for candidate in response.candidates:
                reason = models.RecommendedCandidateReason(
                    job_name=candidate.reason.job_name,
                    industry_year=candidate.reason.industry_year,
                    company_name=candidate.reason.company_name,
                    skill=candidate.reason.skill,
                    topic=candidate.reason.topic,
                    major=candidate.reason.major,
                    school_tags=candidate.reason.school_tags
                )
                recommended_candidate = models.RecommendedCandidate(
                    id=candidate.id,
                    score=candidate.score,
                    reason=reason
                )
                result.append(recommended_candidate)
            return result
        except Exception as e:
            if 'not found' in str(e):
                raise NotFound(f"Not Found: job [{job_id}]")
            raise RemoteServerError(f'Recommend candidates by job [{job_id}] error') from e
