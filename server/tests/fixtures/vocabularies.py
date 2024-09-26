SDGS = [
    {"qcode": "SDG1", "is_active": True, "name": "End poverty in all its forms everywhere"},
    {
        "qcode": "SDG2",
        "is_active": True,
        "name": "End hunger, achieve food security and improved nutrition and promote " "sustainable agriculture",
    },
    {"qcode": "SDG3", "is_active": True, "name": "Ensure healthy lives and promote well-being for all at all ages"},
    {
        "qcode": "SDG4",
        "is_active": True,
        "name": "Ensure inclusive and equitable quality education and promote lifelong"
        " learning opportunities for all",
    },
    {"qcode": "SDG5", "is_active": True, "name": "Achieve gender equality and empower all women and girls"},
    {
        "qcode": "SDG6",
        "is_active": True,
        "name": "Ensure availability and sustainable management of water and" " sanitation for all",
    },
    {
        "qcode": "SDG7",
        "is_active": True,
        "name": "Ensure access to affordable, reliable, sustainable and modern" " energy for all",
    },
    {
        "qcode": "SDG8",
        "is_active": True,
        "name": "Promote sustained, inclusive and sustainable economic growth,"
        " full and productive employment and decent work for all",
    },
    {
        "qcode": "SDG9",
        "is_active": True,
        "name": "Build resilient infrastructure, promote inclusive and sustainable"
        " industrialization and foster innovation",
    },
    {"qcode": "SDG10", "is_active": True, "name": "Reduce inequality within and among countries"},
    {
        "qcode": "SDG11",
        "is_active": True,
        "name": "Make cities and human settlements inclusive, safe, resilient" " and sustainable",
    },
    {"qcode": "SDG12", "is_active": True, "name": "Ensure sustainable consumption and production patterns"},
    {"qcode": "SDG13", "is_active": True, "name": "Take urgent action to combat climate change and its impacts"},
    {
        "qcode": "SDG14",
        "is_active": True,
        "name": "Conserve and sustainably use the oceans, seas and marine" " resources for sustainable development",
    },
    {
        "qcode": "SDG15",
        "is_active": True,
        "name": "Protect, restore and promote sustainable use of terrestrial"
        " ecosystems, sustainably manage forests, combat desertification,"
        " and halt and reverse land degradation and halt biodiversity loss",
    },
    {
        "qcode": "SDG16",
        "is_active": True,
        "name": "Promote peaceful and inclusive societies for sustainable"
        " development, provide access to justice for all and build"
        " effective, accountable and inclusive institutions at all levels",
    },
]


VOCABULARIES = [
    {
        "_id": "profile_id",
        "field_type": "custom",
        "items": [],
        "type": "manageable",
        "schema": {},
        "service": {"all": 1},
        "custom_field_type": "profile-id",
        "display_name": "Author",
        "unique_field": "qcode",
    },
    {
        "_id": "profile_job_title",
        "field_type": "custom",
        "items": [],
        "type": "manageable",
        "schema": {},
        "service": {"all": 1},
        "custom_field_type": "vocabulary-typeahead-field",
        "custom_field_config": {
            "vocabulary_name": "job_titles",
            "allow_freetext": True,
        },
        "display_name": "Job Title",
        "unique_field": "qcode",
    },
    {
        "_id": "job_titles",
        "display_name": "Job Titles",
        "type": "manageable",
        "selection_type": "single selection",
        "unique_field": "qcode",
        "schema": {"qcode": {}, "name": {}},
        "items": [
            {"qcode": "ceo", "name": "CEO", "is_active": True},
            {"qcode": "director", "name": "Director", "is_active": True},
            {"qcode": "media_advisor", "name": "Media Advisor", "is_active": True},
        ],
    },
    {
        "_id": "profile_first_name",
        "field_type": "custom",
        "items": [],
        "type": "manageable",
        "schema": {},
        "service": {"all": 1},
        "custom_field_type": "profile-text",
        "display_name": "First Name",
    },
    {
        "_id": "profile_last_name",
        "field_type": "custom",
        "items": [],
        "type": "manageable",
        "schema": {},
        "service": {"all": 1},
        "custom_field_type": "profile-text",
        "display_name": "Last Name",
    },
    {
        "_id": "profile_private_text",
        "field_type": "custom",
        "items": [],
        "type": "manageable",
        "schema": {},
        "service": {"all": 1},
        "custom_field_type": "profile-text",
        "custom_field_config": {
            "exclude_from_content_api": True,
        },
        "display_name": "Last Name",
    },
    {
        "_id": "sdg",
        "display_name": "SDGs",
        "type": "manageable",
        "unique_field": "qcode",
        "selection_type": "single selection",
        "schema": {
            "qcode": {"required": True},
            "name": {"required": True},
        },
        "items": SDGS,
    },
    {
        "_id": "profile_sdg_a",
        "display_name": "Sustainable Development Goals",
        "field_type": "custom",
        "service": {"all": 1},
        "custom_field_type": "vocabulary-field",
        "custom_field_config": {
            "vocabulary_name": "sdg",
            "allow_freetext": False,
            "exclude_from_content_api": False,
        },
        "items": [],
        "schema": {},
    },
    {
        "_id": "profile_sdg_b",
        "display_name": "Sustainable Development Goals",
        "field_type": "custom",
        "service": {"all": 1},
        "custom_field_type": "vocabulary-field",
        "custom_field_config": {
            "vocabulary_name": "sdg",
            "allow_freetext": False,
            "exclude_from_content_api": False,
        },
        "items": [],
        "schema": {},
    },
]

CONTENT_TYPES = [
    {
        "_id": "article",
        "label": "Article",
        "enabled": True,
        "editor": {
            "slugline": {
                "order": 1,
                "sdWidth": "full",
                "enabled": True,
                "required": True,
            },
            "profile_id": None,
        },
        "schema": {
            "slugline": {
                "type": "string",
                "required": True,
                "maxlength": 24,
                "nullable": False,
            },
            "profile_id": None,
        },
    },
    {
        "_id": "author_profile",
        "label": "Author Profile",
        "enabled": True,
        "editor": {
            "profile_id": {
                "enabled": True,
                "field_name": "Author",
                "order": 1,
                "section": "header",
                "required": True,
            },
            "profile_job_title": {
                "enabled": True,
                "field_name": "Job Title",
                "order": 2,
                "section": "content",
                "required": False,
            },
            "profile_first_name": {
                "enabled": True,
                "field_name": "First Name",
                "order": 3,
                "section": "content",
                "required": True,
            },
            "profile_last_name": {
                "enabled": True,
                "field_name": "Last Name",
                "order": 4,
                "section": "content",
                "required": True,
            },
            "profile_private_text": {
                "enabled": True,
                "field_name": "Private Text",
                "order": 5,
                "section": "content",
                "required": False,
            },
            "profile_sdg_a": {
                "enabled": True,
                "field_name": "SDGs",
                "order": 6,
                "section": "content",
                "required": False,
            },
            "profile_sdg_b": {
                "enabled": True,
                "field_name": "SDGs",
                "order": 7,
                "section": "content",
                "required": False,
            },
        },
        "schema": {
            "profile_id": {
                "type": "custom",
                "required": True,
                "enabled": True,
                "nullable": False,
            },
            "profile_job_title": {
                "type": "custom",
                "required": False,
                "enabled": True,
                "nullable": True,
            },
            "profile_first_name": {
                "type": "custom",
                "required": False,
                "enabled": True,
                "nullable": True,
            },
            "profile_last_name": {
                "type": "custom",
                "required": False,
                "enabled": True,
                "nullable": True,
            },
            "profile_private_text": {
                "type": "custom",
                "required": False,
                "enabled": True,
                "nullable": True,
            },
            "profile_sdg_a": {
                "type": "custom",
                "required": False,
                "enabled": True,
                "nullable": True,
            },
            "profile_sdg_b": {
                "type": "custom",
                "required": False,
                "enabled": True,
                "nullable": True,
            },
        },
    },
]

TEST_USER = {
    "_id": "abcd123",
    "username": "foobar",
    "first_name": "Foo",
    "last_name": "Bar",
    "user_type": "user",
    "display_name": "Foo Bar",
    "is_enabled": True,
    "is_active": True,
}
