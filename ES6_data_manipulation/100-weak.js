// weakMap.js
export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  if (!weakMap.has(endpoint)) {
    weakMap.set(endpoint, 0);
  }

  const queryCount = weakMap.get(endpoint);
  if (queryCount >= 4) { // Se lanza error cuando es >= 5 en la próxima consulta
    throw new Error('Endpoint load is high');
  }

  weakMap.set(endpoint, queryCount + 1);
}
