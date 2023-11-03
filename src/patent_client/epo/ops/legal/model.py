import datetime
from dataclasses import dataclass
from dataclasses import field
from typing import Optional

from patent_client.epo.ops.number_service.model import DocumentId
from patent_client.util import Model
from yankee.data import ListCollection


@dataclass
class MetaData(Model):
    status_of_data: Optional[str] = None
    docdb_publication_number: Optional[str] = None
    subscriber_exchange_date: Optional[datetime.date] = None
    epo_created_date: Optional[datetime.date] = None
    docdb_integer: Optional[int] = None


@dataclass
class LegalEvent(Model):
    """
    Field descriptions are here:
    https://documents.epo.org/projects/babylon/eponot.nsf/0/EF223017D933B30AC1257B50005A042E/$File/14.11_User_Documentation_3.1_en.pdf

    """

    filing_or_publication: Optional[str] = None
    document_number: Optional[str] = None
    ip_type: Optional[str] = None
    metadata: Optional[MetaData] = None
    country_code: Optional[str] = None
    text_record: Optional[str] = None

    event_date: Optional[datetime.date] = None
    event_code: Optional[str] = None
    event_country: Optional[str] = None
    event_description: Optional[str] = None
    regional_event_code: Optional[str] = None

    corresponding_patent: Optional[str] = None
    corresponding_patent_publication_date: Optional[datetime.date] = None

    designated_states: Optional[str] = None
    extension_name: Optional[str] = None
    new_owner_name: Optional[str] = None
    free_text: Optional[str] = None
    spc_number: Optional[str] = None
    spc_filing_date: Optional[str] = None
    expiry: Optional[str] = None
    publication_language: Optional[str] = None
    inventor_name: Optional[str] = None
    ipc_class: Optional[str] = None
    representative_name: Optional[str] = None
    payment_date: Optional[str] = None
    opponent_name: Optional[str] = None
    year_of_fee_payment: Optional[str] = None
    name_of_requester: Optional[str] = None
    date_extension_granted: Optional[str] = None
    extension_states: Optional[str] = None
    effective_date: Optional[datetime.date] = None
    date_of_withdrawal: Optional[str] = None

    def __repr__(self):
        return f"Event(document_number={self.document_number}, event_description={self.event_description}, event_date={self.event_date})"


@dataclass
class Legal(Model):
    __manager__ = "patent_client.epo.ops.legal.manager.LegalManager"
    publication_reference: Optional[DocumentId] = None
    events: list = field(default_factory=ListCollection)
