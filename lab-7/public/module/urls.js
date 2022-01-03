class Urls {
  constructor() {
    this.url = 'http://localhost:8000/api';
  }

  disks() {
    return `/disks/`;
  }

  disk(id) {
    return `/disks/${id}/`;
  }
}

const urls = new Urls();

export default urls; 
