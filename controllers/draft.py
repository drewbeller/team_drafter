# coding: utf8
import ast

def generate_picks():
    # load draft parameters
    draft_order = db(db.draft_parameter.draft_parameter == 'Draft Order').select().first()['draft_parameter_value']
    rounds = int(db(db.draft_parameter.draft_parameter == 'Rounds').select().first()['draft_parameter_value'])
    # pick_times = db(db.draft_parameter.draft_parameter == 'Pick Time').select().first()['draft_parameter_value']
    # pick_times = ast.literal_eval(pick_times)

    # select all teams and add to dict with id and order
    teams = db(db.team).select(orderby=db.team.team_order)

    db(db.pick).delete()
    pick_num = 0
    for round in range(rounds):
        round_num = round + 1 # round starts at zero
        if (round_num % 2 == 0) and (draft_order == 'snake'):
            teams = teams.sort(lambda team: team.team_order, reverse=True)
        else:
            teams = teams.sort(lambda team: team.team_order)
        print round_num
        for team in teams:
            pick_num = pick_num + 1
            pick_id = db.pick.insert(pick_num=pick_num, pick_round=round_num, pick_team=team)

    session.flash = "Draft Board is ready for %s teams and %s rounds!" % (len(teams), rounds)
    redirect(URL('appadmin', 'manage/league')) ##table-pick

def manage_draft():
    #picks = db(db.pick).select(orderby=db.pick.id)

    fields = [db.pick.id, db.pick.pick_num, db.pick.pick_round, db.pick.pick_team, db.pick.pick_owner, db.pick.pick_player, 
              db.player.player_first_name, db.player.player_last_name, db.player.player_position, db.player.player_pro_team]
    picks = db(db.pick).select(*fields, left=[db.player.on(db.pick.pick_player == db.player.id)])

    teams = db(db.team).select(orderby=db.team.team_order)
    rounds = int(db(db.draft_parameter.draft_parameter == 'Rounds').select().first()['draft_parameter_value'])
    if request.get_vars['pick'] is None:
        request.get_vars['pick'] = 1
    pick_id = db(db.pick.pick_num == request.get_vars['pick']).select().first().id
    form=crud.update(db.pick, pick_id, deletable=False)
    if form.accepts(request.vars, session):
        redirect(URL('manage_draft', vars=dict(pick=int(request.get_vars['pick'])+1)))

    if (int(request.get_vars['pick'])<11):
        pick_time = 180
    elif (int(request.get_vars['pick'])<131):
        pick_time = 90
    else:
        pick_time = 30
    
    return dict(picks=picks, teams=teams, rounds=rounds, form=form, pick_time=pick_time)

def trade_pick():
    return dict(message=T('Hello World'))

def trade_player():
    return dict(message=T('Hello World'))
