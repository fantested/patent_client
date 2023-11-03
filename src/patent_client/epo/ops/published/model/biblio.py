from dataclasses import dataclass
from dataclasses import field
from typing import Optional

from patent_client.epo.ops.number_service.model import DocumentId
from patent_client.epo.ops.util import InpadocModel
from patent_client.util import Model
from yankee.data import ListCollection


@dataclass
class Citation(InpadocModel):
    cited_phase: Optional[str] = None
    cited_by: Optional[str] = None
    epodoc: Optional[DocumentId] = None
    docdb: Optional[DocumentId] = None
    original: Optional[DocumentId] = None

    def __repr__(self):
        return f"Citation(doc_number={str(self.docdb)}, cited_by={self.cited_by}, cited_phase={self.cited_phase})"

    @property
    def docdb_number(self):
        return str(self.docdb)


@dataclass
class Title(Model):
    lang: str
    text: str

    def __repr__(self) -> str:
        return f"Title(lang={self.lang}, text={self.text})"


def limit_text(string, limit=30):
    if len(string) < limit:
        return string
    else:
        return f"{string[:limit]}..."


@dataclass
class InpadocBiblio(InpadocModel):
    __manager__ = "patent_client.epo.ops.published.manager.BiblioManager"
    country: Optional[str] = None
    doc_number: Optional[str] = None
    kind: Optional[str] = None
    family_id: Optional[str] = None
    publication_number: Optional[str] = None
    application_number: Optional[str] = None
    publication_reference_docdb: Optional[DocumentId] = None
    publication_reference_epodoc: Optional[DocumentId] = None
    publication_reference_original: Optional[DocumentId] = None
    application_reference_docdb: Optional[DocumentId] = None
    application_reference_epodoc: Optional[DocumentId] = None
    application_reference_original: Optional[DocumentId] = None
    intl_class: "ListCollection[str]" = field(default_factory=list)
    cpc_class: "ListCollection[str]" = field(default_factory=list)
    us_class: "ListCollection[str]" = field(default_factory=list)
    priority_claims: "ListCollection[str]" = field(default_factory=list)
    title: Optional[str] = None
    titles: "ListCollection[Title]" = field(default_factory=list)
    abstract: Optional[str] = None
    citations: "ListCollection[Citation]" = field(default_factory=list)
    applicants_epodoc: "ListCollection[str]" = field(default_factory=list)
    applicants_original: "ListCollection[str]" = field(default_factory=list)
    inventors_epodoc: "ListCollection[str]" = field(default_factory=list)
    inventors_original: "ListCollection[str]" = field(default_factory=list)
    # TODO: NPL citations

    def __repr__(self):
        return f"InpadocBiblio(publication_number={self.publication_number}, title={limit_text(self.title, 30)})"

    @property
    def docdb_number(self):
        return str(self.publication_reference_docdb)


@dataclass
class BiblioResult(Model):
    documents: list = field(default_factory=list)
