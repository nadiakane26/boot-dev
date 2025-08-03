can_invite = 0b1000
can_kick = 0b0100
can_enter_dungeon = 0b0010
can_surrender = 0b0001


def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    combined =  glorfindel | galadriel | elendil | elrond
    return combined