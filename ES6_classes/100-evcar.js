import Car from './10-car';

export default class EVcar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this._range = range;
  }

  get range() {
    return this._range;
  }

  // Setter para range
  set range(newRange) {
    this._range = newRange;
  }

  // Override de cloneCar para devolver una instancia de Car
  cloneCar() {
    return new Car(this._brand, this._motor, this._color);
  }
}
