from django.core.mail import EmailMultiAlternatives
from django.template import Context
#from django.template import Template
from django.template.loader import get_template

from lizard_damage.models import DamageScenario
from lizard_task.task import task_logging
from celery.task import task
from django.contrib.sites.models import Site

import logging


@task
@task_logging
def send_email(damage_scenario_id, username=None, taskname=None, loglevel=20,
               mail_template='email_received', subject='Onderwerp'):
    logger = logging.getLogger(taskname)
    # Do your thing
    logger.info("send_mail: %s" % mail_template)
    damage_scenario = DamageScenario.objects.get(pk=damage_scenario_id)

    #subject = 'Schademodule: Scenario "%s" ontvangen' % damage_scenario.name
    try:
        root_url = 'http://%s' % Site.objects.all()[0].domain
    except:
        root_url = 'http://damage.lizard.net'
        logger.error('Error fetching Site... defaulting to damage.lizard.net')
    context = Context({"damage_scenario": damage_scenario, 'ROOT_URL': root_url})
    template_text = get_template("lizard_damage/%s.txt" % mail_template)
    template_html = get_template("lizard_damage/%s.html" % mail_template)

    from_email = 'no-reply@nelen-schuurmans.nl'
    to = damage_scenario.email

    logger.info("scenario: %s" % damage_scenario)
    logger.info("sending e-mail to: %s" % to)
    msg = EmailMultiAlternatives(subject, template_text.render(context), from_email, [to])
    msg.attach_alternative(template_html.render(context), 'text/html')
    msg.send()

    logger.info("e-mail has been successfully sent")


@task
@task_logging
def calculate_damage(damage_scenario_id, username=None, taskname=None, loglevel=20):
    """
    Main calculation task.
    """
    logger = logging.getLogger(taskname)
    logger.info("calculate damage")
    damage_scenario = DamageScenario.objects.get(pk=damage_scenario_id)
    logger.info("scenario: %d, %s" % (damage_scenario.id, str(damage_scenario)))

    logger.info("finished")
