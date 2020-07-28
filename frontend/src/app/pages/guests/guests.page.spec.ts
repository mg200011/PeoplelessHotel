import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { GuestsPage } from './guests.page';

describe('GuestsPage', () => {
  let component: GuestsPage;
  let fixture: ComponentFixture<GuestsPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GuestsPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(GuestsPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
