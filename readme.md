
# Integrator

This code calculates triple integrals using cylindrical coordinates. The entire process of solving for the triple integral is shown below.

First, we need to calculate the Jacobian for cylindrical coordinates. This is given by:

J(r,θ,z) = r

Next, we need to choose our limits of integration. In this case, we will integrate from 0 to 2π for θ, from 0 to 1 for r, and from 0 to 2 for z.

With these limits of integration, we can now write out the triple integral in cylindrical coordinates:

∫∫∫ J(r,θ,z)drdθdz

= ∫∫∫ rdrdθdz

= ∫∫ rdθdr

= ∫ rdrdθ

= ∫ r²dθdr

= ∫ 0→2π ∫ 0→1 r²dθdr

= ∫ 0→2π ∫ 0→1 r²dθdr

= ∫ 0→2π ∫ 0→1 r²sin