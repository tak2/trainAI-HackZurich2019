package com.example.hackzurich.database

import com.google.firebase.database.FirebaseDatabase
import com.google.firebase.database.ValueEventListener

/**
 * Created by Amr on 9/28/2019.
 */
class FirebaseDatabaseManager constructor(private val database: FirebaseDatabase) {


    fun getTechnicianTickets(listener:ValueEventListener) {
        val reference = database.reference
        reference.addValueEventListener(listener)
    }

}