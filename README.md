# Reading Material

 - [PW User Guide](http://www.quantum-espresso.org/wp-content/uploads/Doc/pw_user_guide.pdf) make sure to read sections 3.1, 3.3, 3.4
 - [PW Input File Description](http://www.quantum-espresso.org/wp-content/uploads/Doc/INPUT_PW.html) MUST READ!

# Degugging Notes:
 1. Always read CRASH file. It will have information on why the calculation ended
 2. `ecutwfc` is in units of Rydbergs ~ 13.6 eV. For ultrasoft potentials use 8-12. For others aim for 400-500 eV.x
 3. If calculcation is `vc-relax` or `vc-md` it requires namelist &CELL to be defined...
 4. If you have to make many adjustments for your calculation to converge look at changing the pseudo potential
 5. Make sure to use 'verified' pseudo potentials. I have found that some do not work (especially the unverified ones)
