-- b329 -- THE AXIOM PROBE. Run by tools/b329_axiom_probe.py; its stdout is data/b329_axiom_probe.txt.
-- Which tactics and which core lemmas carry axioms, measured and not assumed.
-- (1) tactics
theorem t_omega (a b : Nat) (h : a < b) : a + 1 ≤ b := by omega
theorem t_acrfl (u p q : Nat) : p * (u * q) = u * (q * p) := by ac_rfl
theorem t_simp (u p : Nat) : u = u * p ^ 0 := by simp
theorem t_rwiff (u p : Nat) (h : Nat.gcd u p = 1) : Nat.Coprime u p := by rw [Nat.coprime_iff_gcd_eq_one]; exact h
theorem t_bycases_dvd (p t : Nat) : p ∣ t ∨ ¬ p ∣ t := by
  by_cases h : p ∣ t
  · exact Or.inl h
  · exact Or.inr h
theorem t_obtain (p t : Nat) (h : p ∣ t) : ∃ k, t = p * k := by
  obtain ⟨k, hk⟩ := h
  exact ⟨k, hk⟩
theorem t_strong : ∀ t : Nat, 0 < t → 0 < t := by
  intro t
  induction t using Nat.strongRecOn with
  | _ t ih => intro h; exact h
theorem t_rw (a b : Nat) (h : a = b) : a + 0 = b := by rw [Nat.add_zero, h]
theorem t_rcases (p q : Prop) (h : p ∨ q) : q ∨ p := by
  rcases h with h | h
  · exact Or.inr h
  · exact Or.inl h
theorem t_decide : (List.range 10).all (fun x => x < 10) = true := by decide
theorem t_cases_deceq (t p : Nat) : t = p ∨ t ≠ p := by
  cases Nat.decEq t p with
  | isTrue h => exact Or.inl h
  | isFalse h => exact Or.inr h
#print axioms t_omega
#print axioms t_acrfl
#print axioms t_simp
#print axioms t_rwiff
#print axioms t_bycases_dvd
#print axioms t_obtain
#print axioms t_strong
#print axioms t_rw
#print axioms t_rcases
#print axioms t_decide
#print axioms t_cases_deceq
-- (2) the core lemmas the first draft leaned on (the registration's probed names), and the ones the module uses
#print axioms Nat.Coprime.pow_right
#print axioms Nat.Coprime.dvd_of_dvd_mul_left
#print axioms Nat.Coprime.symm
#print axioms Nat.coprime_iff_gcd_eq_one
#print axioms Nat.gcd_dvd_left
#print axioms Nat.gcd_dvd_right
#print axioms Nat.dvd_trans
#print axioms Nat.dvd_sub
#print axioms Nat.dvd_mul_left
#print axioms Nat.eq_one_of_dvd_one
#print axioms Nat.mod_eq_zero_of_dvd
#print axioms Nat.dvd_of_mod_eq_zero
#print axioms Nat.sub_one_mul
#print axioms Nat.sub_mod_eq_zero_of_mod_eq
#print axioms Nat.mod_eq_of_lt
#print axioms Nat.eq_zero_of_dvd_of_lt
#print axioms Nat.mul_mod_mod
#print axioms Nat.mul_assoc
#print axioms Nat.mul_sub
#print axioms Nat.mul_sub_one
#print axioms Nat.div_add_mod
#print axioms Nat.mod_mod_of_dvd
#print axioms Nat.pow_dvd_pow
#print axioms Nat.dvd_refl
#print axioms Nat.add_mul
#print axioms Nat.pow_add
#print axioms Nat.pow_mul
#print axioms Nat.add_left_cancel
#print axioms Nat.add_right_cancel
#print axioms Nat.succ_ne_zero
#print axioms List.all_eq_true
#print axioms Bool.and_eq_true
#print axioms Nat.dvd_iff_mod_eq_zero
-- (3) the axiom-free core names the module rests on
#print axioms Nat.pow_pos
#print axioms Nat.zero_mod
#print axioms Nat.one_mul
#print axioms Nat.pow_succ
#print axioms Nat.pow_zero
#print axioms Nat.mul_one
#print axioms Nat.mul_zero
#print axioms Nat.zero_mul
#print axioms Nat.mul_succ
#print axioms Nat.succ_mul
#print axioms Nat.mul_add
#print axioms Nat.mul_comm
#print axioms Nat.add_comm
#print axioms Nat.add_assoc
#print axioms Nat.add_zero
#print axioms Nat.add_succ
#print axioms Nat.add_right_comm
#print axioms Nat.two_mul
#print axioms Nat.eq_of_mul_eq_mul_right
#print axioms Nat.pow_le_pow_right
#print axioms Nat.mul_le_mul_right
#print axioms Nat.lt_of_not_le
#print axioms Nat.pos_of_ne_zero
#print axioms Nat.lt_of_lt_of_le
#print axioms Nat.le_trans
#print axioms Nat.lt_irrefl
#print axioms Nat.le_antisymm
#print axioms Nat.zero_le
#print axioms Nat.le_refl
#print axioms Nat.le_succ_of_le
#print axioms Nat.le_of_lt_succ
#print axioms Nat.eq_or_lt_of_le
#print axioms Nat.lt_or_ge
#print axioms Nat.lt_add_of_pos_right
#print axioms Nat.le_add_left
#print axioms Nat.eq_zero_of_add_eq_zero_right
#print axioms Nat.decEq
#print axioms Nat.succ.inj
#print axioms Nat.strongRecOn
#print axioms List.Mem
#print axioms congrArg
