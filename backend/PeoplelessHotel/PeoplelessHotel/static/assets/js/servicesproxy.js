'use strict';

class ServicesProxy {

    async getReservations() {
        const s = new Services();
        let list = await s.gget("/reservations/get_user_reservations/");
        return list;
    }

    async getReservation(resrv) {
        const s = new Services();
        let list = await s.gget(`/reservations/get_user_reservation_by_id/${resrv}/`);
        return list[0];
    }

    
    async updateReservation(resrv) {
        const s = new Services();
        let list = await s.gput(`/reservations/${resrv.id}`, resrv);
        return list;
    }


    async getRooms() {
        const s = new Services();
        return await s.gget("/rooms");
    }

    async createPersonGroup(reserveid) {
        const s = new Services();
        let res = await s.gget(`/guests/create_person_group/${reserveid}/`);
        console.log(res);
        return res;
    }

    
    async createPersonGroup(reserveid, guestid) {
        const s = new Services();
        let resrv = await this.getReservation(reserveid);
        let url = `/guests/add_person_to_group/${resrv.person_group_id}/${guestid}/`;
        console.log(url);        
        let res = await s.gget(url);
        console.log(res);
        return res;
    }

    
    async trainPersonGroup(reserveid) {
        const s = new Services();
        let resrv = await this.getReservation(reserveid);
        let url = `/guests/train_person_group/${resrv.person_group_id}/`; 
        console.log(url);        
        let res = await s.gget(url);
        console.log(res);
        return res;
    }


    
    async verifyPerson(roomid, image) {
        const s = new Services();
        let url = `/guests/identify_in_person_group/${room_id}/`; 
        console.log(url);        
        let res = await s.gpost(url, { image: image } );
        console.log(res);
        return res;
    }

    
    

    

}
