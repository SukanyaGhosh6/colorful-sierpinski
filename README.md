# Sierpinski Triangle — A Colorful Fractal with Python Turtle

##  Project Overview

This project generates a vibrant, colorful version of the famous **Sierpiński Triangle** fractal using **Python's Turtle graphics**.  
It’s a fun demonstration of how **recursion** and **simple geometry** can create beautifully intricate designs!

The idea is simple yet magical: by repeatedly subdividing triangles into smaller triangles and coloring them randomly, we create an endlessly fascinating pattern — all with just a few lines of code.

---

##  Features

- Recursive drawing of the Sierpiński triangle
- Randomized colorful palette for each sub-triangle
- Smooth, fast rendering using Python's `turtle` module
- Fully dynamic: change the recursion level to control the complexity

---

##  How It Works

1. **Start with a large triangle** on the screen.
2. **Split it into three smaller triangles** by connecting midpoints.
3. **Recursively repeat** the process for each new triangle.
4. **Randomly fill colors** from a beautiful palette to make each triangle vibrant.
5. **Base case:** when the recursion depth hits 0, simply draw a triangle.

This process perfectly visualizes how recursion works: "solve a smaller version of the same problem."

---

##  Technologies Used

- **Language:** Python 3.x
- **Library:** Turtle (built-in Python library)
- **Concepts:** Recursion, Geometry, Randomized Coloring

---

##  How to Run

1. Make sure you have **Python 3.x** installed.
2. No external libraries are needed — `turtle` and `random` come built-in.
3. Copy the code into a Python file, e.g., `sierpinski.py`.
4. Run the script:

```bash
python sierpinski.py
```

5. Enjoy watching the fractal art unfold!

---

##  Customize

- **Change recursion level**:  
  Higher levels → more detail (but slower).  
  Lower levels → simpler patterns.

  ```python
  sierpinski(t, points, level=5)  # Try 4, 6, or even 7
  ```

- **Change color palette**:  
  Modify the `palette` list with your favorite colors.

- **Resize the triangle**:  
  Adjust the `size` variable inside the `main()` function.

---

##  Preview

*(Add a screenshot if you want!)*

Example output:  
A colorful, mesmerizing Sierpiński Triangle drawn live on your screen.

---

##  What I Learned

- How recursion can be used for real-world visual projects
- How geometric concepts like midpoints build fractals
- How simple colors and randomness can turn math into art
- Better understanding of how Turtle graphics work in Python

---

##  References

- [Sierpinski Triangle - Wikipedia](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle)
- [Python Turtle Graphics Documentation](https://docs.python.org/3/library/turtle.html)

---

##  Author

**Sukanya Ghosh**  

---

##  License

This project is licensed under the **MIT License** — free to use, modify, and have fun with!

