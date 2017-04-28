# osencryption
A modified version of the SHA1 algorithms.
Python has this built in, but this is being coded from scratch so it can be modified to fit user's need.
The SHA1 has four main functions through which 80 32-bit words run through.  Each function is assigned 20 words to operate on.
The four functions use several bitwise operators to find a unique output (in my code I call it "f").
I deviated from the SHA1 as my "f" outputs arent cumulative, and instead reset after each function. 

<h1>Usage</h1>
<p>pip install collections <br>
python sha1f.py
</p>

<h1>Future progress</h1>
<p>I will use arrays instead of lists, as they are much faster. <br>
A complete overhaul of variable naming, and class structure is needed. <br>
Better modification will be implemented as my knowledge of hashing algorithms grows. <br>
</p>
