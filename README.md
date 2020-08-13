# Mesoor 推荐系统 Python SDK
* 安装  
    ```shell script
    pip install -r requirements.txt
    python -m grpc_tools.protoc -I protos --python_betterproto_out=. protos/* 
    pip install .
    ```
* 使用
    ```python
    from mesoor_recommendation_sdk import models, MesoorRecommendation
    service = MesoorRecommendation('localhost:50051')
    ```
    ```python
    # 保存 Job
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
    job_id = 'foo_id'
    await service.save_job(
        id=job_id,
        job=job
    )
    ```
    ```python
    # 保存 Candidate
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

    candidate_id = 'foo_id'
    await service.save_candidate(
        id=candidate_id,
        candidate=candidate
    )
    ```
    ```python
    # 获取按 Job 推荐的 Candidate
    job_id = 'foo_id'
    result = await service.recommend_candidates_by_job(job_id=job_id)
    ```