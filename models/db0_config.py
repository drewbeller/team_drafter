# coding: utf8
auth.settings.create_user_groups = False
auth.settings.auth_manager_role = 'Manager'

auth.settings.manager_actions = dict(
    coaches=dict(role='Manager', tables=[db.auth_user, db.auth_membership]),
    db=dict(role='Administrator', heading='Manage Database', tables=db.tables),
    league=dict(role='Commissioner', tables=['team', 'draft_parameter', 'pick', 'player'])
)
