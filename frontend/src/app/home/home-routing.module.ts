import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomePage } from './home.page';

const routes: Routes = [
  {
    path: 'home',
    component: HomePage,
    children:[
      {
        path:'guests',
        loadChildren:()=>
        import('../pages/guests/guests.module').then(
          m=>m.GuestsPageModule
        )
      },
      {
        path:'reservations',
        loadChildren:()=>
        import('../pages/reservations/reservations.module').then(
          m=>m.ReservationsPageModule
        )
      },
      {
        path:'settings',
        loadChildren:()=>
        import('../pages/settings/settings.module').then(
          m=>m.SettingsPageModule
        )
      },
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class HomePageRoutingModule {}
