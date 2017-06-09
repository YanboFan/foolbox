import numpy as np

from foolbox.attacks import DeepFool as Attack


def test_attack(bn_adversarial):
    adv = bn_adversarial
    attack = Attack()
    attack(adv)
    assert adv.get() is not None
    assert adv.best_distance().value() < np.inf


def test_attack_gl(gl_bn_adversarial):
    adv = gl_bn_adversarial
    attack = Attack()
    attack(adv)
    assert adv.get() is None
    assert adv.best_distance().value() == np.inf


def test_targeted_attack(bn_targeted_adversarial):
    adv = bn_targeted_adversarial
    attack = Attack()
    attack(adv)
    assert adv.get() is None
    assert adv.best_distance().value() == np.inf


def test_subsample(bn_adversarial):
    adv = bn_adversarial
    attack = Attack()
    attack(adv, subsample=5)
    assert adv.get() is not None
    assert adv.best_distance().value() < np.inf


def test_attack_impossible(bn_impossible):
    adv = bn_impossible
    attack = Attack()
    attack(adv)
    assert adv.get() is None
    assert adv.best_distance().value() == np.inf