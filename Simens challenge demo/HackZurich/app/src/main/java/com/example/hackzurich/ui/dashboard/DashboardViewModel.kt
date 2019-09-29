package com.example.hackzurich.ui.dashboard

import android.util.Log
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.hackzurich.database.FirebaseDatabaseManager
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.DatabaseError
import com.google.firebase.database.FirebaseDatabase
import com.google.firebase.database.ValueEventListener

class DashboardViewModel : ViewModel() {
    private val firebaseDatabase = FirebaseDatabase.getInstance()


    private val tickets = MutableLiveData<MutableList<Ticket>>()
    fun getTickets(): MutableLiveData<MutableList<Ticket>> {
        val list = FirebaseDatabaseManager(firebaseDatabase).getTechnicianTickets(object :
            ValueEventListener {
            override fun onDataChange(dataSnapshot: DataSnapshot) {
                // Get Post object and use the values to update the UI
                // ...
                if (dataSnapshot.hasChild("tickets")) {
                    val memberList = dataSnapshot.child("tickets").value as ArrayList<*>
                    tickets.value = parseTickets(memberList)
                }
            }

            override fun onCancelled(databaseError: DatabaseError) {
                // Getting Post failed, log a message
                // ...
                Log.i("Tag", "failure")

            }
        })

        return tickets
    }

    fun parseTickets(UserDataList: ArrayList<*>): ArrayList<Ticket> {
        val size = UserDataList.size
        var index = 0
        val userList = ArrayList<Ticket>()

        while (index < size) {
            val hashMap: HashMap<*, *> = UserDataList[index] as HashMap<*, *>
            val id = hashMap["ticketId"] as Long
            val name = hashMap["ticketName"].toString()
            val desc = hashMap["ticketDesc"].toString()
            val longitude: Double = hashMap["longitude"] as Double
            val latitude: Double = hashMap["latitude"] as Double
            userList.add(
                Ticket(
                    ticketId = id,
                    ticketName = name,
                    ticketDesc = desc,
                    longitude = longitude,
                    latitude = latitude
                )
            )
            index++
        }
        return userList
    }
}