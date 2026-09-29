# __init__.py
# This file makes the config directory a package

from .courses import (
    COURSES_BY_CATEGORY,
    RESUME_VIDEOS,
    INTERVIEW_VIDEOS,
    get_courses_for_role,
    get_category_for_role
)

from .job_roles import JOB_ROLES

from .database import (
    get_database_connection,
    init_database,
    save_resume_data,
    save_analysis_data,
    get_resume_stats,
    log_admin_action,
    get_admin_logs,
    get_all_resume_data,
    verify_admin,
    add_admin
)

# Initialize the database when the package is loaded
init_database()

__all__ = [
    "COURSES_BY_CATEGORY",
    "RESUME_VIDEOS",
    "INTERVIEW_VIDEOS",
    "get_courses_for_role",
    "get_category_for_role",
    "get_database_connection",
    "init_database",
    "save_resume_data",
    "save_analysis_data",
    "get_resume_stats",
    "log_admin_action",
    "get_admin_logs",
    "get_all_resume_data",
    "verify_admin",
    "add_admin"
]
