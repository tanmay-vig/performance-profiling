
# Performance Profiling of Sorting Algorithms on Large Datasets

## 📌 Project Overview

This project performs a comparative analysis of five sorting algorithms—**Quick Sort**, **Merge Sort**, **Heap Sort**, **Bubble Sort**, and Python’s built-in **Timsort**—on randomly generated large datasets. The goal is to measure and visualize **execution time** and **memory usage** to understand the practical performance trade-offs of each algorithm.

---

## 🎯 Objectives

- Evaluate the scalability of different sorting algorithms.
- Measure execution time and memory consumption.
- Visualize and compare algorithm performance on large datasets.

---

## 🧪 Algorithms Covered

- Quick Sort
- Merge Sort
- Heap Sort
- Bubble Sort
- Timsort (`sorted()` function in Python)

---

## 🛠️ Technologies & Tools Used

| Tool/Library     | Purpose                             |
|------------------|--------------------------------------|
| Python 3.10+     | Core language for development        |
| `time`           | Measure execution time               |
| `tracemalloc`    | Track memory usage                   |
| `random`         | Generate randomized datasets         |
| `matplotlib`     | Plot performance graphs              |
| `numpy` (optional) | Numerical support (for consistency) |

---

## 📊 Dataset

- Random integer arrays generated using `random.sample()`
- Sizes Tested: `1000`, `5000`, `10000`, `20000`, `40000`
- Range: Each dataset contains values in the range `[0, 2*N]` where `N` is the number of elements

---

## 📈 Output

- **Execution Time Graph** for all algorithms across different input sizes
- **Memory Usage Graph** for each algorithm
- Skips Bubble Sort for sizes > 5000 due to impractical runtime

---

## ▶️ How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/sorting-algorithm-profiling.git
   cd sorting-algorithm-profiling
   ```

2. **Install dependencies**

   ```bash
   pip install matplotlib numpy
   ```

3. **Run the script**

   ```bash
   python sort_profiler.py
   ```

---

## 📌 Sample Results

* Timsort (Python’s built-in `sorted()`) showed the best overall performance
* Merge Sort was consistent but used slightly more memory
* Quick Sort had variable performance depending on data distribution
* Heap Sort was reliable but memory-heavy in some cases
* Bubble Sort was only feasible for very small datasets

---

## 📚 References

* Cormen et al., *Introduction to Algorithms*, MIT Press
* Tim Peters, PEP 450 - Timsort
* R. Sedgewick, *Algorithms in C++*
* Sharma et al., “Comparative Analysis of Sorting Algorithms,” IJCA, 2020

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change or improve.

