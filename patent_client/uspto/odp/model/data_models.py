from pydantic import Field, AliasPath, BeforeValidator, model_validator
import datetime
from typing import Optional
from typing_extensions import Annotated

from patent_client.util.related import get_model
from . import BaseODPModel

# Common

class Address(BaseODPModel):
    city_name: Optional[str] = Field(alias="cityName", default=None)
    geographic_region_name: Optional[str] = Field(alias="geographicRegionName", default=None)
    geographic_region_code: Optional[str] = Field(alias="geographicRegionCode", default=None)
    country_code: Optional[str] = Field(alias="countryCode", default=None)
    postal_code: Optional[str] = Field(alias="postalCode", default=None)
    country_name: Optional[str] = Field(alias="countryName", default=None)
    address_line_one_text: Optional[str] = Field(alias="addressLineOneText", default=None)
    address_line_two_text: Optional[str] = Field(alias="addressLineTwoText", default=None)
    name_line_one_text: Optional[str] = Field(alias="nameLineOneText", default=None)
    name_line_two_text: Optional[str] = Field(alias="nameLineTwoText", default=None)
    postal_address_category: Optional[str] = Field(alias="postalAddressCategory", default=None)
    correspondent_name_text: Optional[str] = Field(alias="correspondentNameText", default=None)

# Continuity

class Relationship(BaseODPModel):
    application_status_code: int = Field()
    claim_type_code: str = Field(alias="claimParentageTypeCode")
    filing_date: datetime.date
    application_status_description: str = Field(alias="applicationStatusDescriptionText")
    claim_type_description: str = Field(alias="claimParentageTypeCodeDescription")
    parent_application_id: str = Field(alias="parentApplicationNumberText")
    child_application_id: str = Field(alias="childApplicationNumberText")
    
    
class Continuity(BaseODPModel):
    count: int
    request_identifier: str
    parent_continuity: Optional[list[Relationship]] = Field(alias=AliasPath(["patentBag", 0, "continuityBag", "parentContinuityBag"]), default=None)
    child_continuity: Optional[list[Relationship]] = Field(alias=AliasPath(["patentBag", 0, "continuityBag", "childContinuityBag"]), default=None)

# Documents

class DownloadOption(BaseODPModel):
    mime_type_identifier: str
    download_url: str
    pages: int = Field(alias="pageTotalQuantity")

class Document(BaseODPModel):
    appl_id: str = Field(alias="applicationNumberText")
    mail_date: datetime.datetime = Field(alias="officialDate")
    document_identifier: str = Field(alias="documentIdentifier")
    document_code: str = Field(alias="documentCode")
    document_code_description: str = Field(alias="documentCodeDescriptionText")
    direction_category: str = Field(alias="directionCategory")
    download_option_bag: list[dict] = Field(alias="downloadOptionBag")

# Assignment

class Assignor(BaseODPModel):
    execution_date: datetime.date = Field(alias="executionDate")
    assignor_name: str = Field(alias="assignorName")

class AssigneeAddress(BaseODPModel):
    city_name: str = Field(alias="cityName")
    geographic_region_code: str = Field(alias="geographicRegionCode")
    postal_code: str = Field(alias="postalCode")
    address_line_one_text: str = Field(alias="addressLineOneText")

class Assignee(BaseODPModel):
    assignee_address: AssigneeAddress = Field(alias="assigneeAddress")
    assignee_name_text: str = Field(alias="assigneeNameText")

class Assignment(BaseODPModel):
    assignment_received_date: datetime.date = Field(alias="assignmentReceivedDate")
    frame_number: str = Field(alias="frameNumber")
    page_number: int = Field(alias="pageNumber")
    reel_number_frame_number: str = Field(alias="reelNumber/frameNumber")
    assignment_recorded_date: datetime.date = Field(alias="assignmentRecordedDate")
    conveyance_text: str = Field(alias="conveyanceText")
    assignment_mailed_date: datetime.date = Field(alias="assignmentMailedDate")
    reel_number: str = Field(alias="reelNumber")
    assignor_bag: list[Assignor] = Field(alias="assignorBag")
    assignee_bag: list[Assignee] = Field(alias="assigneeBag")
    correspondence_address: list[Address] = Field(alias="correspondenceAddress")

# Foreign Priority

class ForeignPriority(BaseODPModel):
    priority_number_text: str = Field(alias="priorityNumberText")
    filing_date: datetime.date = Field(alias="filingDate")
    country_name: str = Field(alias="countryName")

# Attorney



class TelecommunicationAddress(BaseODPModel):
    telecommunication_number: str = Field(alias="telecommunicationNumber")
    usage_type_category: str = Field(alias="usageTypeCategory")

class Attorney(BaseODPModel):
    active_indicator: str = Field(alias="activeIndicator")
    first_name: Optional[str] = Field(alias="firstName", default=None)
    last_name: Optional[str] = Field(alias="lastName", default=None)
    registration_number: str = Field(alias="registrationNumber")
    attorney_address_bag: list[Address] = Field(alias="attorneyAddressBag")
    telecommunication_address_bag: list[TelecommunicationAddress] = Field(alias="telecommunicationAddressBag")
    registered_practitioner_category: str = Field(alias="registeredPractitionerCategory")
    name_suffix: Optional[str] = Field(alias="nameSuffix", default=None)

class CustomerNumber(BaseODPModel):
    attorneys: list[Attorney] = Field(alias="attorneyBag")
    customer_number: Optional[str] = Field(alias=AliasPath("customerNumber", "patronIdentifier"))
    address: Optional[Address] = Field(alias=AliasPath("customerNumber", "powerOfAttorneyAddressBag", 0))
   
# Transactions

class Transaction(BaseODPModel):
    recorded_date: datetime.date = Field(alias="recordedDate")
    transaction_code: str = Field(alias="caseActionCode")
    transaction_description: str = Field(alias="caseActionDescriptionText")
 
# Adjustment Data
class TermAdjustmentHistory(BaseODPModel):
    applicant_day_delay_quantity: int = Field(alias="applicantDayDelayQuantity")
    start_sequence_number: float = Field(alias="startSequenceNumber")
    case_action_description_text: str = Field(alias="caseActionDescriptionText")
    case_action_sequence_number: float = Field(alias="caseActionSequenceNumber")
    action_date: datetime.date = Field(alias="actionDate")

class TermAdjustment(BaseODPModel):
    applicant_day_delay_quantity: Optional[int] = Field(alias="applicantDayDelayQuantity", default=None)
    overlapping_day_quantity: Optional[int] = Field(alias="overlappingDayQuantity", default=None)
    filing_date: Optional[datetime.date] = Field(alias="filingDate", default=None)
    c_delay_quantity: Optional[int] = Field(alias="cDelayQuantity", default=None)
    adjustment_total_quantity: Optional[int] = Field(alias="adjustmentTotalQuantity", default=None)
    b_delay_quantity: Optional[int] = Field(alias="bDelayQuantity", default=None)
    grant_date: Optional[datetime.date] = Field(alias="grantDate", default=None)
    a_delay_quantity: Optional[int] = Field(alias="aDelayQuantity", default=None)
    non_overlapping_day_quantity: Optional[int] = Field(alias="nonOverlappingDayQuantity", default=None)
    ip_office_day_delay_quantity: Optional[int] = Field(alias="ipOfficeDayDelayQuantity", default=None)
    history: Optional[list[TermAdjustmentHistory]] = Field(alias="patentTermAdjustmentHistoryDataBag", default=None)

# Application Object

YNBool = Annotated[bool, BeforeValidator(lambda v: v == "Y")]


class Inventor(BaseODPModel):
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    full_name: str = Field(alias="inventorNameText")
    addresses: list[Address] = Field(alias="correspondenceAddressBag")

class Applicant(BaseODPModel):
    applicant_name: str = Field(alias="applicantNameText")
    addresses: list[Address] = Field(alias="correspondenceAddressBag")
    app_status_code: int = Field(alias="applicationStatusCode")
    app_status: str = Field(alias="applicationStatusDescriptionText")
    
    
    
class ApplicationBiblio(BaseODPModel):
    aia_indicator: YNBool = Field(alias="firstInventorToFileIndicator")
    app_filing_date: datetime.date = Field(alias="filingDate")
    inventors: list[Inventor] = Field(alias="inventorBag")
    customer_number: int = Field(alias="customerNumber")
    group_art_unit: str = Field(alias="groupArtUnitNumber")
    invention_title: str = Field(alias="inventionTitle")
    correspondence_address: list[Address] = Field(alias="correspondenceAddressBag")
    app_conf_num: int = Field(alias="applicationConfirmationNumber")
    atty_docket_num: str = Field(alias="docketNumber")
    appl_id: str = Field(alias="applicationNumberText")
    first_inventor_name: str = Field(alias="firstInventorName")
    first_applicant_name: str = Field(alias="firstApplicantName")
    cpc_classifications: list[str] = Field(alias="cpcClassificationBag")
    entity_status: str = Field(alias="businessEntityStatusCategory")
    app_early_pub_number: Optional[str] = Field(alias="earliestPublicationNumber")
    
    
class Application(ApplicationBiblio):
    app_type_code: str = Field(alias="applicationTypeCode")
    national_stage_indicator: YNBool = Field(alias="nationalStageIndicator")
    
    effective_filing_date: datetime.date = Field(alias="effectiveFilingDate")
    cls_sub_cls: str = Field(alias="class/subclass")
    assignments: list[Assignment] = Field(alias="assignmentBag")
    attorneys: CustomerNumber = Field(alias="recordAttorney")
    transactions: list[Transaction] = Field(alias="transactionContentBag")
    parent_applications: Optional[list[Relationship]] = Field(alias=AliasPath("continuityBag", "parentContinuityBag"), default=None)
    child_applications: Optional[list[Relationship]] = Field(alias=AliasPath("continuityBag", "childContinuityBag"), default=None)
    patent_term_adjustment: Optional[TermAdjustment] = Field(alias="patentTermAdjustmentData")
    
    @model_validator(mode="before")
    @classmethod
    def _validate_patent_term_adjustment(cls, v):
        if v['patentTermAdjustmentData'] == dict():
            v['patentTermAdjustmentData'] = None
        return v
    
## RESPONSE Models

class SearchResult(BaseODPModel):
    filing_date: datetime.date
    appl_id: str = Field(alias="applicationNumberText")
    invention_title: str = Field(alias="inventionTitle")
    filing_date: datetime.date = Field(alias="filingDate")
    patent_number: Optional[str] = Field(alias="patentNumber", default=None)
    
    @property
    def bibliographic_data(self) -> ApplicationBiblio:
        return get_model("patent_client.uspto.odp.model.ApplicationBiblio").objects.get(appl_id=self.appl_id)
    
    @property
    def application(self) -> Application:
        return get_model("patent_client.uspto.odp.model.Application").objects.get(appl_id=self.appl_id)
    
    @property
    def continuity(self) -> Continuity:
        return get_model("patent_client.uspto.odp.model.Continuity").objects.get(appl_id=self.appl_id)
    
    @property
    def documents(self) -> list[Document]:
        return get_model("patent_client.uspto.odp.model.Document").objects.filter(appl_id=self.appl_id)

    # Aliases
    @property
    def biblio(self) -> ApplicationBiblio:
        return self.bibliographic_data
    
    @property
    def app(self) -> Application:
        return self.application
    
    @property
    def docs(self) -> list[Document]:
        return self.documents


class SearchResponse(BaseODPModel):
    count: int
    results: list[SearchResult] = Field(alias="patentBag")
    request_id: str = Field(alias="requestIdentifier")