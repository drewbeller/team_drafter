# coding: utf8

db.auth_user._singular = 'Coach'
db.auth_user._plural = 'Coaches'

db.auth_membership._singular = 'Role'
db.auth_membership._plural = 'Roles'

db.define_table('team',
                Field('team_name'),
                Field('team_coach', 'reference auth_user'),
                Field('team_order'),
                format="%(team_name)s"
                )

db.define_table('player',
                 Field('player_first_name'),
                 Field('player_last_name'),
                 Field('player_pro_team'),
                 Field('player_position'),
                 Field('player_id'),
                 Field('player_description',
                     compute=lambda r: "%s, %s (%s, %s)" % (r['player_last_name'], r['player_first_name'], r['player_position'], r['player_pro_team'])
                     ),
                 format='%(player_last_name)s, %(player_first_name)s (%(player_position)s, %(player_pro_team)s)'
                 )

db.define_table('pick',
                Field('pick_num', type='integer'),
                Field('pick_round', type='integer'),
                Field('pick_team', 'reference team'),
                Field('pick_owner', 'reference team'),
                Field('pick_player', 'reference player')
                )
db.pick.pick_num.writable = False
db.pick.pick_round.writable = False
db.pick.pick_team.writable = False
#db.pick.pick_player.widget = SQLFORM.widgets.autocomplete(
#     request, db.player.player_description, id_field=db.player.id)

db.define_table('draft_parameter',
                Field('draft_parameter'),
                Field('draft_parameter_value'),
                Field('draft_parameter_comment')
                )
db.draft_parameter.draft_parameter.writable = False
db.draft_parameter.draft_parameter_comment.writable = False
