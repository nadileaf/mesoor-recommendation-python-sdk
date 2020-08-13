from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List, Dict

from com.mesoor.mesoor_recommendation import sdk


class Degree(Enum):
    不限 = -4
    初中 = -2
    中专 = -1
    高中 = 0
    专科 = 8
    本科 = 16
    硕士 = 24
    博士 = 32
    博士后 = 40


class Status(Enum):
    ACTIVE = 1  # 正常状态
    ARCHIVE = 2  # 归档状态（已删除）


@dataclass
class JobDetail:
    """
    职位信息。如果属性有默认值，可留空。
    """
    # 职位名
    name: str
    # 职位描述
    description: str
    # 公司
    employer: str
    # 学历要求
    degree: Degree = Degree.不限
    # 工作经验要求（年）
    years: int = 0
    # 薪酬下限
    salary_low: int = 0
    # 薪酬上限
    salary_high: int = 0
    # 职位发布时间戳(ms)
    publish_date_ts: Optional[int] = None
    # 职位过期时间戳(ms)
    expire_date_ts: Optional[int] = None
    # 职位所属行业（如果有层级结构用`::`隔开。如: `互联网::电子商务`）
    industries: List[str] = field(default_factory=list)
    # 工作地点代码 [行政区划代码](http://www.mca.gov.cn/article/sj/xzqh/2018/201804-12/20181201301111.html)
    location_ids: List[int] = field(default_factory=list)
    # 职位所属部门
    department: Optional[str] = None
    # 职位类别 (如果有层级结构用`::`隔开。如: `互联网::电子商务`)
    categories: List[str] = field(default_factory=list)

    def to_sdk_representation(self) -> sdk.JobDetail:
        return sdk.JobDetail(
            name=self.name,
            description=self.description,
            employer=self.employer,
            publish_date_ts=self.publish_date_ts,
            expire_date_ts=self.expire_date_ts,
            industries=self.industries,
            location_ids=self.location_ids,
            department=self.department,
            years=self.years,
            degree=self.degree.value,
            salary_low=self.salary_low,
            salary_high=self.salary_high,
            categories=self.categories
        )


@dataclass
class ResumeBasic:
    """
    简历基本信息
    """
    # 候选人当前所在地点代码 [行政区划代码](http://www.mca.gov.cn/article/sj/xzqh/2018/201804-12/20181201301111.html)
    location_id: Optional[int] = None
    # 候选人生日时间戳(ms)
    birthday_ts: Optional[int] = None

    def to_sdk_representation(self) -> sdk.ResumeBasic:
        return sdk.ResumeBasic(
            location_id=self.location_id,
            birthday_ts=self.birthday_ts
        )


@dataclass
class ResumeWork:
    """
    简历工作信息
    """
    # 职位名
    position: Optional[str] = None
    # 公司
    company: Optional[str] = None
    # 工作经历描述
    description: Optional[str] = None
    # 工作部门
    department: Optional[str] = None
    # 工作所属行业（如果有层级结构用`::`隔开。如: `互联网::电子商务`）
    industry: Optional[str] = None
    # 工作职责
    responsibility: Optional[str] = None
    # 工作开始时间戳(ms)
    start_date_ts: Optional[int] = None
    # 工作结束时间戳(ms)
    end_date_ts: Optional[int] = None
    # 是否持续至今
    until_now: bool = False

    def to_sdk_representation(self) -> sdk.ResumeWork:
        return sdk.ResumeWork(
            position=self.position,
            company=self.company,
            description=self.description,
            department=self.department,
            industry=self.industry,
            responsibility=self.responsibility,
            start_date_ts=self.start_date_ts,
            end_date_ts=self.end_date_ts,
            until_now=self.until_now
        )


@dataclass
class ResumeProject:
    """
    简历项目信息
    """
    # 职位名
    position: Optional[str] = None
    # 项目名
    name: Optional[str] = None
    # 公司
    company: Optional[str] = None
    # 工作经历描述
    description: Optional[str] = None
    # 工作部门
    department: Optional[str] = None
    # 工作职责
    responsibility: Optional[str] = None
    # 工作开始时间戳(ms)
    start_date_ts: Optional[int] = None
    # 工作结束时间戳(ms)
    end_date_ts: Optional[int] = None
    # 是否持续至今
    until_now: bool = False

    def to_sdk_representation(self) -> sdk.ResumeProject:
        return sdk.ResumeProject(
            position=self.position,
            name=self.name,
            company=self.company,
            description=self.description,
            department=self.department,
            responsibility=self.responsibility,
            start_date_ts=self.start_date_ts,
            end_date_ts=self.end_date_ts,
            until_now=self.until_now
        )


@dataclass
class ResumeIntern:
    """
    简历实习信息
    """
    # 职位名
    position: Optional[str] = None
    # 公司
    company: Optional[str] = None
    # 工作经历描述
    description: Optional[str] = None
    # 工作部门
    department: Optional[str] = None
    # 工作职责
    responsibility: Optional[str] = None
    # 工作开始时间戳(ms)
    start_date_ts: Optional[int] = None
    # 工作结束时间戳(ms)
    end_date_ts: Optional[int] = None
    # 是否持续至今
    until_now: bool = False

    def to_sdk_representation(self) -> sdk.ResumeIntern:
        return sdk.ResumeIntern(
            position=self.position,
            company=self.company,
            description=self.description,
            department=self.department,
            responsibility=self.responsibility,
            start_date_ts=self.start_date_ts,
            end_date_ts=self.end_date_ts,
            until_now=self.until_now
        )


@dataclass
class ResumeEducation:
    """
    简历教育信息
    """
    # 专业
    major: Optional[str] = None
    # 学历
    degree: Optional[Degree] = None
    # 学校名
    school: Optional[str] = None
    # 工作开始时间戳(ms)
    start_date_ts: Optional[int] = None
    # 工作结束时间戳(ms)
    end_date_ts: Optional[int] = None
    # 是否持续至今
    until_now: bool = False

    def to_sdk_representation(self) -> sdk.ResumeEducation:
        return sdk.ResumeEducation(
            major=self.major,
            degree=self.degree.name,
            school=self.school,
            start_date_ts=self.start_date_ts,
            end_date_ts=self.end_date_ts,
            until_now=self.until_now
        )


@dataclass
class Resume:
    basic: "ResumeBasic" = field(default_factory=ResumeBasic)
    works: List["ResumeWork"] = field(default_factory=list)
    projects: List["ResumeProject"] = field(default_factory=list)
    interns: List["ResumeIntern"] = field(default_factory=list)
    educations: List["ResumeEducation"] = field(default_factory=list)
    # 简历更新时间
    update_date_ts: Optional[int] = None

    def to_sdk_representation(self) -> sdk.Resume:
        return sdk.Resume(
            works=[i.to_sdk_representation() for i in self.works],
            projects=[i.to_sdk_representation() for i in self.projects],
            interns=[i.to_sdk_representation() for i in self.interns],
            educations=[i.to_sdk_representation() for i in self.educations],
            basic=self.basic.to_sdk_representation()
        )


@dataclass
class Job:
    job_detail: "JobDetail"
    status: Status = Status.ACTIVE

    def to_sdk_representation(self):
        return sdk.Job(
            job_detail=self.job_detail.to_sdk_representation(),
            status=self.status.value
        )


@dataclass
class Candidate:
    resume: "Resume"
    status: Status = Status.ACTIVE

    def to_sdk_representation(self):
        return sdk.Candidate(
            resume=self.resume.to_sdk_representation(),
            status=self.status.value
        )


@dataclass
class RecommendedCandidateReason:
    # 候选人满足要求的职位名
    job_name: List[str]
    # 候选人满足要求的行业及年限
    industry_year: Dict[str, int]
    # 候选人满足的要求的公司名
    company_name: List[str]
    # 候选人满足要求的技能词
    skill: List[str]
    # 候选人满足要求的领域词
    topic: List[str]
    # 候选人满足要求的专业
    major: List[str]
    # 候选人满足要求的学校标签
    school_tags: List[str]


@dataclass
class RecommendedCandidate:
    id: str
    score: float
    reason: "RecommendedCandidateReason"
