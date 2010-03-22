# -*- coding: utf-8 -*-
"""Setup the thingsoup application"""
import logging

from thingsoup.config.environment import load_environment
from thingsoup import model
from thingsoup.model import meta

from thingsoup.model.thing import Thing
from thingsoup.model.dcmi import DCMI_point

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup thingsoup here"""
    load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    log.info("Creating tables …")
    meta.metadata.create_all(bind=meta.engine)
    log.info("Successfully set up.")

    log.info("Adding example thing …")
    thing = Thing(title="Eiffel Tower", description="A 19th century iron lattice tower located on the Champ de Mars in Paris that has become both a global icon of France.")
    meta.Session.add(thing)
    meta.Session.commit()
    log.info("Successfully added example thing.")

    log.info("Adding example location …")
    location = DCMI_point(east="2.2945", north="48.8583", name="Champ de Mars")
    meta.Session.add(location)
    meta.Session.commit()
    log.info("Successfully added example location.")
