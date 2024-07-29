class HolbertonCourse {
  constructor(name, length, students) {
    // check atri.
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    if (!Array.isArray(students) || !students.every((student) => typeof student === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }

    // under line names
    this._name = HolbertonCourse._validateName(name);
    this._length = HolbertonCourse._validateName(length);
    this._students = HolbertonCourse._validateName(students);
  }

  // Getter y Setter for name
  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = HolbertonCourse._validateName(newName);
  }

  // Getter y Setter for length
  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof newLength !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = HolbertonCourse._validateName(newLength);
  }

  // Getter y Setter for students
  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (!Array.isArray(newStudents) || !newStudents.every((student) => typeof student === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = HolbertonCourse._validateName(newStudents);
  }
}

export default HolbertonCourse;
