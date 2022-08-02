from collections import namedtuple

from housing.entity.config_entity import DataValidationConfig

DataIngestionArtifact = namedtuple("DataIngestionArtifact",[
"train_file_path","test_file_path","is_ingested","message"
])

DataValidationArtifact = namedtuple("DataValidationArtifact",
["schema_file_path","report_file_path","report_page_file_path","is_validated","message"])

                                    