__author__ = 'mahajrod'

from Pantera.Tools.Annotation.SNPeff import SNPeff
from Pantera.Tools.Annotation.Barrnap import Barrnap
from Pantera.Tools.Annotation.AUGUSTUS import AUGUSTUS
from Pantera.Tools.Annotation.Exonerate import Exonerate
from Pantera.Tools.Annotation.TransDecoder import TransDecoder

SNPeff_path = ""
SNPeff = SNPeff(jar_path=SNPeff_path)

Barrnap = Barrnap()
AUGUSTUS = AUGUSTUS()
Exonerate = Exonerate()
TransDecoder = TransDecoder()
