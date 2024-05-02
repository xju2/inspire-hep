from dataclasses import dataclass


@dataclass
class PaperData:
    texkeys: str
    citation_count: int
    citation_count_without_self_citations: int
    doi: str
    arxiv_eprints: str
    arxiv_category: str
    preprint_date: str
    title: str
    bibtex: str
    inspire_id: str
    authors: str
    cite_info: str

    def __post_init__(self):
        assert self.title, "Title cannot be empty."
        assert self.authors, "Authors cannot be empty."
