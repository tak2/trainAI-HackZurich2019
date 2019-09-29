package com.example.hackzurich.ui.dashboard

/**
 * Created by Amr on 9/28/2019.
 */
data class Ticket(
    val antennaId: String="",
    val longitude: Double=0.0,
    val latitude: Double=0.0,
    val ticketId: Long=0,
    val ticketName: String="",
    val ticketDesc: String=""
)