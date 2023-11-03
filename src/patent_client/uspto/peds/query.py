from dataclasses import dataclass
from dataclasses import fields


@dataclass
class QueryFields:
    app_type_facet: str = "appTypeFacet"
    appl_id: str = "applId"
    total_pto_days: str = "totalPtoDays"
    app_filing_date: str = "appFilingDate"
    first_named_applicant_address: str = "firstNamedApplicantAddress"
    app_location_facet: str = "appLocationFacet"
    app_location_date: str = "appLocationDate"
    inventor_name: str = "inventorName"
    app_early_pub_date: str = "appEarlyPubDate"
    intl_filing_year: str = "intlFilingYear"
    app_exam_mdl_name: str = "appExamMdlName"
    pta_pte_type: str = "ptaPteType"
    corr_addr_name_line_two: str = "corrAddrNameLineTwo"
    app_location: str = "appLocation"
    app_early_pub_number: str = "appEarlyPubNumber"
    wipo_early_pub_date: str = "wipoEarlyPubDate"
    id: str = "id"
    text: str = "text"
    app_trans_history_date: str = "appTransHistoryDate"
    primary_inventor_city: str = "primaryInventorCity"
    app_exam_last_name: str = "appExamLastName"
    first_named_applicant_name_list: str = "firstNamedApplicantNameList"
    app_pubyear: str = "appPubyear"
    app_sub_cls: str = "appSubCls"
    primary_inventor_country: str = "primaryInventorCountry"
    patent_number_facet: str = "patentNumberFacet"
    app_status: str = "appStatus"
    corr_addr_street_line_two: str = "corrAddrStreetLineTwo"
    pta_pte_ind: str = "ptaPteInd"
    corr_addr_geo_region_na: str = "corrAddrGeoRegionNA"
    first_named_applicant_address_list: str = "firstNamedApplicantAddressList"
    first_inventor_file_facet: str = "firstInventorFileFacet"
    c_delay: str = "cDelay"
    app_status_date: str = "appStatusDate"
    app_control_number: str = "appControlNumber"
    pto_adjustments: str = "ptoAdjustments"
    first_inventor_file: str = "firstInventorFile"
    app_grp_art_number_facet: str = "appGrpArtNumberFacet"
    overlap_delay: str = "overlapDelay"
    app_type: str = "appType"
    rank_and_inventors_list: str = "rankAndInventorsList"
    app_status_year: str = "appStatusYear"
    primary_inventor_middle_name: str = "primaryInventorMiddleName"
    pct_app_type: str = "pctAppType"
    app_cust_number: str = "appCustNumber"
    last_updated_timestamp: str = "lastUpdatedTimestamp"
    first_named_applicant_facet: str = "firstNamedApplicantFacet"
    wipo_early_pub_number: str = "wipoEarlyPubNumber"
    app_cls_sub_cls: str = "appClsSubCls"
    b_delay: str = "bDelay"
    corr_addr_name_line_one: str = "corrAddrNameLineOne"
    first_named_applicant: str = "firstNamedApplicant"
    app_exam_first_name: str = "appExamFirstName"
    patent_number_str: str = "patentNumberStr"
    app_pct_number: str = "appPCTNumber"
    corr_addr_country_cd: str = "corrAddrCountryCd"
    pto_delay: str = "ptoDelay"
    app_trans_history_desc: str = "appTransHistoryDesc"
    app_entity_status: str = "appEntityStatus"
    app_location_year: str = "appLocationYear"
    corr_addr_country_name: str = "corrAddrCountryName"
    app_early_pub_year: str = "appEarlyPubYear"
    app_exam_name: str = "appExamName"
    public_ind: str = "publicInd"
    app_cls_sub_cls_facet: str = "appClsSubClsFacet"
    app_exam_name_facet: str = "appExamNameFacet"
    primary_inventor_first_name: str = "primaryInventorFirstName"
    pct_app_type_facet: str = "pctAppTypeFacet"
    intl_filing_date: str = "intlFilingDate"
    primary_inventor_facet: str = "primaryInventorFacet"
    app_entity_status_txt: str = "appEntityStatus_txt"
    app_grp_art_number: str = "appGrpArtNumber"
    patent_kind_code: str = "patentKindCode"
    app_filing_year: str = "appFilingYear"
    app_attr_dock_number_facet: str = "appAttrDockNumberFacet"
    primary_inventor_region: str = "primaryInventorRegion"
    first_named_applicant_name: str = "firstNamedApplicantName"
    appl_id_txt: str = "appl_id_txt"
    patent_term_json: str = "patentTermJson"
    patent_number: str = "patentNumber"
    last_mod_ts_utc: str = "LAST_MOD_TS_UTC"
    app_cls: str = "appCls"
    last_insert_time: str = "LAST_INSERT_TIME"
    patent_issue_year: str = "patentIssueYear"
    app_status_txt: str = "appStatus_txt"
    app_cust_number_facet: str = "appCustNumberFacet"
    app_intl_pub_date: str = "appIntlPubDate"
    app_early_pub_number_facet: str = "appEarlyPubNumberFacet"
    patent_title: str = "patentTitle"
    appl_delay: str = "applDelay"
    appl_id_str: str = "applIdStr"
    app_pct_number_facet: str = "appPCTNumberFacet"
    app_attr_dock_number: str = "appAttrDockNumber"
    primary_inventor: str = "primaryInventor"
    app_pub_seq_number: str = "appPubSeqNumber"
    corr_addr_street_line_one: str = "corrAddrStreetLineOne"
    ip_office_code: str = "ipOfficeCode"
    a_delay: str = "aDelay"
    rank_and_inventors_list_str: str = "rankAndInventorsList_str"
    app_intl_pub_number_facet: str = "appIntlPubNumberFacet"
    publish_doc_json: str = "publishDocJson"
    rank_and_inventors_address_list: str = "rankAndInventorsAddressList"
    corr_addr_postal_code: str = "corrAddrPostalCode"
    app_intl_pub_year: str = "appIntlPubYear"
    primary_inventor_last_name: str = "primaryInventorLastName"
    patent_issue_date: str = "patentIssueDate"
    app_intl_pub_number: str = "appIntlPubNumber"
    app_control_number_facet: str = "appControlNumberFacet"
    corr_addr_cust_no: str = "corrAddrCustNo"
    corr_addr_city: str = "corrAddrCity"
    app_exam_prefrd_name: str = "appExamPrefrdName"
    app_confr_number: str = "appConfrNumber"

    @classmethod
    def field_names(cls):
        return [f.name for f in fields(cls)]

    @classmethod
    def is_date_field(cls, field_name):
        return any(field_name in f for f in cls._date_fields)

    @classmethod
    def get(cls, key):
        return getattr(cls, key)

    _date_fields = [
        "appFilingDate",
        "appLocationDate",
        "appEarlyPubDate",
        "wipoEarlyPubDate",
        "appTransHistoryDate",
        "appStatusDate",
        "lastUpdatedTimestamp",
        "intlFilingDate",
        "LAST_MOD_TS_UTC",
        "LAST_INSERT_TIME",
        "appIntlPubDate",
        "patentIssueDate",
    ]
