def solution(bandage, health, attacks):
    casting_time, recovery_per_sec, bonus_recovery = bandage
    cur_health = health
    time_diff = 0
    last_attack = 0

    for attack_time, damage in attacks:
        time_diff = attack_time - last_attack
        last_attack = attack_time
        succeeded_casting = time_diff - 1

        recovery = succeeded_casting * recovery_per_sec + succeeded_casting // casting_time * bonus_recovery

        cur_health = min(cur_health + recovery, health) - damage

        if cur_health <= 0:
            return -1

    return cur_health
