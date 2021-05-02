from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, portrait, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
import yaml

TEMPLATE_PDF = "template/tmpl_marriage_registration.pdf"
RESULT_PDF = "result.pdf"
CONFIG_PATH = "config.yaml"
pdfmetrics.registerFont(TTFont("ipaexm", 'fonts/ipaexm.ttf'))
pdfmetrics.registerFont(TTFont("ipaexg", 'fonts/ipaexg.ttf'))


def setup():
    cc = canvas.Canvas(RESULT_PDF, pagesize=landscape(A3))
    page = PdfReader(TEMPLATE_PDF, decompress=False).pages
    pp = pagexobj(page[0])
    cc.doForm(makerl(cc, pp))
    return cc


def load_config():
    with open("../config.yaml", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    return cfg


def husband_name_info(cfg, cc):
    cc.setFont("ipaexm", 24)
    x, y = cfg["last_name_pos"]
    cc.drawString(x, y, cfg["last_name"])
    cc.setFont("ipaexm", 12)
    x, y = cfg["last_name_kana_pos"]
    cc.drawString(x, y, cfg["last_name_kana"])
    cc.setFont("ipaexm", 24)
    x, y = cfg["first_name_pos"]
    cc.drawString(x, y, cfg["first_name"])
    cc.setFont("ipaexm", 12)
    x, y = cfg["first_name_kana_pos"]
    cc.drawString(x, y, cfg["first_name_kana"])
    cc.setFont("ipaexm", 12)
    cc.drawString(221, 569, str(cfg["birth_year"]))
    cc.drawString(300, 569, str(cfg["birth_month"]))
    cc.drawString(345, 569, str(cfg["birth_day"]))
    return cc


def husband_address_info(cfg, cc):
    cc.setFont("ipaexm", 12)
    x, y = cfg["address_first_pos"]
    cc.drawString(x, y, str(cfg["address_first"]))
    cc.drawString(x - 12, y - 21, str(cfg["address_second"]))
    if cfg["is_banchi_address"]:
        cc.ellipse(300, 539, 270, 528)
    else:
        cc.circle(279.5, 523, 6)
    cc.drawString(x + 80, y - 21, str(cfg["address_go"]))
    cc.drawString(x + 10, y - 44, str(cfg["household_person"]))
    cc.setFont("ipaexm", 5)
    y -= 13
    for text in cfg["address_apartment"].split("\n"):
        cc.drawString(x+130, y, text)
        y -= 5
    return cc


def husband_legally_domiciled_info(cfg, cc):
    cc.setFont("ipaexm", 12)
    x, y = cfg["legally_domiciled_first_pos"]
    cc.drawString(x, y, str(cfg["legally_domiciled_first"]))
    cc.drawString(x, y - 21, str(cfg["legally_domiciled_second"]))
    if cfg["is_banchi_legally_domiciled"]:
        cc.ellipse(346, 473, 316, 462)
    else:
        cc.circle(327, 457, 6)
    cc.drawString(x + 10, y - 44, str(cfg["head_of_person_of_legally_domiciled"]))
    return cc


def husband_family_info(cfg, cc):
    cc.setFont("ipaexm", 12)
    x, y = cfg["father_name_pos"]
    cc.drawString(x, y, str(cfg["father_name"]))
    x, y = cfg["mother_name_pos"]
    cc.drawString(x, y, str(cfg["mother_name"]))


def wife_name_info(cfg, cc):
    cc.setFont("ipaexm", 24)
    x, y = cfg["last_name_pos"]
    cc.drawString(x, y, cfg["last_name"])
    cc.setFont("ipaexm", 12)
    x, y = cfg["last_name_kana_pos"]
    cc.drawString(x, y, cfg["last_name_kana"])
    cc.setFont("ipaexm", 24)
    x, y = cfg["first_name_pos"]
    cc.drawString(x, y, cfg["first_name"])
    cc.setFont("ipaexm", 12)
    x, y = cfg["first_name_kana_pos"]
    cc.drawString(x, y, cfg["first_name_kana"])
    cc.setFont("ipaexm", 12)
    cc.drawString(421, 569, str(cfg["birth_year"]))
    cc.drawString(500, 569, str(cfg["birth_month"]))
    cc.drawString(545, 569, str(cfg["birth_day"]))
    return cc


def wife_address_info(cfg, cc):
    cc.setFont("ipaexm", 12)
    x, y = cfg["address_first_pos"]
    cc.drawString(x, y, str(cfg["address_first"]))
    cc.drawString(x - 12, y - 21, str(cfg["address_second"]))
    if cfg["is_banchi_address"]:
        cc.ellipse(502, 539, 472, 528)
    else:
        cc.circle(481, 523, 6)
    cc.drawString(x + 80, y - 21, str(cfg["address_go"]))
    cc.drawString(x + 10, y - 44, str(cfg["household_person"]))
    cc.setFont("ipaexm", 5)
    y -= 13
    for text in cfg["address_apartment"].split("\n"):
        cc.drawString(x+130, y, text)
        y -= 5
    return cc


def wife_legally_domiciled_info(cfg, cc):
    cc.setFont("ipaexm", 12)
    x, y = cfg["legally_domiciled_first_pos"]
    cc.drawString(x, y, str(cfg["legally_domiciled_first"]))
    cc.drawString(x, y - 21, str(cfg["legally_domiciled_second"]))
    if cfg["is_banchi_legally_domiciled"]:
        cc.ellipse(549, 473, 519, 462)
    else:
        cc.circle(327, 457, 6)
    cc.drawString(x + 10, y - 44, str(cfg["head_of_person_of_legally_domiciled"]))
    return cc


def wife_family_info(cfg, cc):
    cc.setFont("ipaexm", 12)
    x, y = cfg["father_name_pos"]
    cc.drawString(x, y, str(cfg["father_name"]))
    x, y = cfg["mother_name_pos"]
    cc.drawString(x, y, str(cfg["mother_name"]))


def new_new_legally_domiciled(cfg, cc):
    cc.setFont("ipaexm", 12)
    if cfg["is_husband_lastname"]:
        cc.rect(196, 351, 5, 5, fill=True)
    else:
        cc.rect(196, 340, 5, 5, fill=True)


def main():
    cc = setup()
    cfg = load_config()
    husband_name_info(cfg["husband"], cc)
    husband_address_info(cfg["husband"], cc)
    husband_legally_domiciled_info(cfg["husband"], cc)
    husband_family_info(cfg["husband"], cc)
    wife_name_info(cfg["wife"], cc)
    wife_address_info(cfg["wife"], cc)
    wife_legally_domiciled_info(cfg["wife"], cc)
    wife_family_info(cfg["wife"], cc)
    new_new_legally_domiciled(cfg["new_legally_domiciled"], cc)
    cc.showPage()
    cc.save()


if __name__ == "__main__":
    main()
