from odoo import models, fields, api



class ResGroups(models.Model):
   _inherit = 'res.groups'

   def get_application_groups(self, domain):
      group_id = self.env.ref('project.group_project_recurring_tasks').id
      group_id_substask = self.env.ref('project.group_subtask_project').id
      return super(ResGroups, self).get_application_groups(domain + [('id','not in', (group_id, group_id_substask))])
