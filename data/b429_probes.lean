import NavierStokes.R3.Theorem

open NavierStokesR3.ProblemStatement NavierStokes.ProblemStatement Set MeasureTheory

/-- PROBE 1. The negated class is INHABITABLE for some force, so
`¬ Nonempty (GlobalFiniteEnergySolution ν f)` is not true of every `f` for free. -/
theorem b429_probe_class_inhabited (ν : ℝ) :
    Nonempty (GlobalFiniteEnergySolution ν (fun _ => 0)) := by
  refine ⟨{ velocity := fun _ => 0
            pressure := fun _ => 0
            velocity_smooth := contDiffOn_const
            pressure_smooth := contDiffOn_const
            zero_initial_velocity := fun x => rfl
            divergence_free := ?_
            navier_stokes := ?_
            energy_bounded := ?_ }⟩
  · intro t _ x
    simp [spatialDivergence, spatialDerivative]
  · intro t _ x
    simp [NavierStokesR3.ProblemStatement.navierStokesResidual, temporalDerivative,
          advection, spatialDerivative, spatialLaplacian, pressureGradient]
  · refine ⟨0, le_refl 0, fun t _ => ⟨?_, ?_⟩⟩
    · simp [SquareIntegrableAtTime]
    · simp [kineticEnergy]

/-- PROBE 2. The blow-up field of `CandidateProperties` REFUSES the zero field, so the
construction half cannot be met by a degenerate witness. -/
theorem b429_probe_blowup_refuses_zero :
    ¬ NavierStokes.ProblemStatement.SpeedUnboundedAtOne (fun _ => (0 : NavierStokes.ProblemStatement.Space)) := by
  intro h
  obtain ⟨t, x, _, _, hM⟩ := h 1 one_pos 1 one_pos
  simp at hM
  exact absurd hM (by norm_num)

#print axioms b429_probe_class_inhabited
#print axioms b429_probe_blowup_refuses_zero
