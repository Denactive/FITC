import DiskComponent from '../../components/disk/disk.js';
import ButtonComponent from '../../components/button/button.js';
import MainPage from '../../pages/main/mainPage.js';
import urls from '../../module/urls.js';
import ajax from '../../module/ajax.js';

export default class DiskPage {
  constructor(root, id) {
    this.root = root;
    this.id = id;
  }

  getData() {
    // return {
    //   id: 1,
    //   src: "https://i.pinimg.com/originals/c9/ea/65/c9ea654eb3a7398b1f702c758c1c4206.jpg",
    //   title: "Акция",
    //   text: "Такой акции вы еще не видели"
    // }
    return ajax.get({url: urls.disk(this.id)});
  }

  get page() {
    return document.getElementById('disk-page');
  }

  getHTML() {
    return (
      `
        <div id="disk-page">
        </div>
      `
    );
  }

  render() {
      this.root.innerHTML = '';
      const html = this.getHTML();
      this.root.insertAdjacentHTML('beforeend', html);

      const disk = new DiskComponent(this.page);
      this.getData().then(({response}) => {
        disk.render(response);

        const backBtn = new ButtonComponent(this.page);
        backBtn.render({sign: 'Назад'}, (e) => {
          const mainPage = new MainPage(this.root);
          mainPage.render();
        });
      });
      
  }
}