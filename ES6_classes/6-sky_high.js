import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft); // call constructor from class 5-building
    this._floors = floors;
  }

  get floors() {
    return this._floors;
  }

  // Override the method:
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
