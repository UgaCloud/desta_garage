from spare.models.garage import Damage


def get_damages():
    return Damage.objects.all()

def get_damage(dmg_id):
    return JobCard.objects.get(pk=dmg_id)