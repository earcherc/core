"""Create new connection models, remove productivity

Revision ID: 33a4f24d9716
Revises: 80ff5f0f9e18
Create Date: 2023-09-01 18:52:56.024426

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "33a4f24d9716"
down_revision = "80ff5f0f9e18"
branch_labels = None
depends_on = None

# Creating ENUM types
gender_enum = postgresql.ENUM(
    "Male",
    "Female",
    "Non-Binary",
    "Transgender",
    "Other",
    "Prefer Not To Say",
    name="gender",
    metadata=sa.MetaData(),
)
connection_status_enum = postgresql.ENUM(
    "Pending", "Accepted", "Blocked", name="connectionstatus", metadata=sa.MetaData()
)


def upgrade() -> None:
    # Create the enum types
    conn = op.get_bind()
    gender_enum.create(conn)
    connection_status_enum.create(conn)

    op.create_table(
        "connection",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_profile1_id", sa.Integer(), nullable=True),
        sa.Column("user_profile2_id", sa.Integer(), nullable=True),
        sa.Column("status", connection_status_enum, nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_profile1_id"],
            ["userprofile.id"],
            name="fk_connection_user_profile1_id",
        ),
        sa.ForeignKeyConstraint(
            ["user_profile2_id"],
            ["userprofile.id"],
            name="fk_connection_user_profile2_id",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_connection_user_profile1_id"),
        "connection",
        ["user_profile1_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_connection_user_profile2_id"),
        "connection",
        ["user_profile2_id"],
        unique=False,
    )
    op.create_table(
        "profilephoto",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_profile_id", sa.Integer(), nullable=True),
        sa.Column("url", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("caption", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("is_main", sa.Boolean(), nullable=False),
        sa.Column("uploaded_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_profile_id"],
            ["userprofile.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_profilephoto_user_profile_id"),
        "profilephoto",
        ["user_profile_id"],
        unique=False,
    )
    op.create_table(
        "userprofiledetails",
        sa.Column("user_profile_id", sa.Integer(), nullable=False),
        sa.Column("bio", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("job_title", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("company", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("school", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("hobbies", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("favorite_music", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("favorite_movies", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("favorite_books", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_profile_id"],
            ["userprofile.id"],
        ),
        sa.PrimaryKeyConstraint("user_profile_id"),
    )
    op.drop_index("ix_studyblock_daily_goal_id", table_name="studyblock")
    op.drop_index("ix_studyblock_study_category_id", table_name="studyblock")
    op.drop_index("ix_studyblock_user_id", table_name="studyblock")
    op.drop_table("studyblock")
    op.drop_index("ix_dailygoal_user_id", table_name="dailygoal")
    op.drop_table("dailygoal")
    op.drop_table("userprofilecategorylink")
    op.drop_index("ix_studycategory_title", table_name="studycategory")
    op.drop_table("studycategory")
    op.add_column(
        "userprofile",
        sa.Column("first_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    )
    op.add_column(
        "userprofile",
        sa.Column("last_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    )
    op.add_column(
        "userprofile", sa.Column("date_of_birth", sa.DateTime(), nullable=True)
    )
    op.add_column(
        "userprofile",
        sa.Column("gender", gender_enum, nullable=True),
    )
    op.add_column(
        "userprofile",
        sa.Column("interested_in_gender", gender_enum, nullable=True),
    )
    op.add_column("userprofile", sa.Column("latitude", sa.Float(), nullable=True))
    op.add_column("userprofile", sa.Column("longitude", sa.Float(), nullable=True))
    op.drop_column("userprofile", "favorite_color")
    op.drop_column("userprofile", "bio")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "userprofile",
        sa.Column("bio", sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "userprofile",
        sa.Column("favorite_color", sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    op.drop_column("userprofile", "longitude")
    op.drop_column("userprofile", "latitude")
    op.drop_column("userprofile", "interested_in_gender")
    op.drop_column("userprofile", "gender")
    op.drop_column("userprofile", "date_of_birth")
    op.drop_column("userprofile", "last_name")
    op.drop_column("userprofile", "first_name")
    op.create_table(
        "studycategory",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('studycategory_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("title", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="studycategory_pkey"),
        postgresql_ignore_search_path=False,
    )
    op.create_index("ix_studycategory_title", "studycategory", ["title"], unique=False)
    op.create_table(
        "userprofilecategorylink",
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            "study_category_id", sa.INTEGER(), autoincrement=False, nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["study_category_id"],
            ["studycategory.id"],
            name="userprofilecategorylink_study_category_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["userprofile.id"], name="userprofilecategorylink_user_id_fkey"
        ),
        sa.PrimaryKeyConstraint(
            "user_id", "study_category_id", name="userprofilecategorylink_pkey"
        ),
    )
    op.create_table(
        "dailygoal",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('dailygoal_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("quantity", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("block_size", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["userprofile.id"], name="dailygoal_user_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="dailygoal_pkey"),
        postgresql_ignore_search_path=False,
    )
    op.create_index("ix_dailygoal_user_id", "dailygoal", ["user_id"], unique=False)
    op.create_table(
        "studyblock",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("start", postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.Column("end", postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.Column("title", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column(
            "rating",
            postgresql.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("daily_goal_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            "study_category_id", sa.INTEGER(), autoincrement=False, nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["daily_goal_id"], ["dailygoal.id"], name="studyblock_daily_goal_id_fkey"
        ),
        sa.ForeignKeyConstraint(
            ["study_category_id"],
            ["studycategory.id"],
            name="studyblock_study_category_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["userprofile.id"], name="studyblock_user_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="studyblock_pkey"),
    )
    op.create_index("ix_studyblock_user_id", "studyblock", ["user_id"], unique=False)
    op.create_index(
        "ix_studyblock_study_category_id",
        "studyblock",
        ["study_category_id"],
        unique=False,
    )
    op.create_index(
        "ix_studyblock_daily_goal_id", "studyblock", ["daily_goal_id"], unique=False
    )
    op.drop_table("userprofiledetails")
    op.drop_index(op.f("ix_profilephoto_user_profile_id"), table_name="profilephoto")
    op.drop_table("profilephoto")
    op.drop_index(op.f("ix_connection_user_profile2_id"), table_name="connection")
    op.drop_index(op.f("ix_connection_user_profile1_id"), table_name="connection")
    op.drop_table("connection")

    # Drop the enum types
    conn = op.get_bind()
    gender_enum.drop(conn)
    connection_status_enum.drop(conn)
