export default class Building {
  constructor(sqft) {
    if (new.target !== Building) {
      this.evacuationWarningMessage();
    }
    // Set the sqft attribute
    this._sqft = sqft;
  }

  // Get for sqft attribute
  get sqft() {
    return this._sqft;
  }

  // Abstract method
  evacuationWarningMessage() {
    if (this) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }
}
