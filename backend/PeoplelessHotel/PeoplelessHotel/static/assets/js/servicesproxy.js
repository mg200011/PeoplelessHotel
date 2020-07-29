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

}
